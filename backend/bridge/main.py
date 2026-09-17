from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from bridge.models import GenerateRequest
from bridge.mcp_client import call_tool

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# Same folder create_project()/create_schematic() write into — kept in one
# place so the download route always looks in exactly the right spot.
GENERATED_DIR = Path(__file__).resolve().parents[2] / "generated_files"


@app.get("/")
def home():

    return {

        "status":
        "AI KiCad Copilot Running"

    }


@app.post("/api/generate")
async def generate(

    request: GenerateRequest
):

    project_name = "demo_board"

    pcb_result = await call_tool(

        "create_kicad_project",

        {

            "project_name":
            project_name

        }

    )

    sch_result = await call_tool(

        "create_kicad_schematic",

        {

            "project_name":
            project_name

        }

    )

    return {

        "prompt":
        request.prompt,

        "message":
        "KiCad project generated",

        "project_name":
        project_name,

        "files":
        [
            f"{project_name}.kicad_pcb",
            f"{project_name}.kicad_sch"
        ],

        "pcb_result":
        pcb_result.content[0].text,

        "schematic_result":
        sch_result.content[0].text
    }


@app.post("/api/header")
async def header():

    result = await call_tool(

        "place_header",

        {

            "pins":4,

            "x_mm":80,

            "y_mm":45,

            "rotation":90

        }

    )

    return {

        "result":
        result.content[0].text

    }


@app.get("/api/download/{project_name}/{filename}")
async def download_file(project_name: str, filename: str):

    file_path = GENERATED_DIR / project_name / filename

    if not file_path.exists():
        return JSONResponse(
            status_code=404,
            content={"error": "File not found"}
        )

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )
