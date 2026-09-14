from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


from bridge.models import GenerateRequest

from bridge.mcp_client import call_tool



# Create FastAPI app

app = FastAPI(
    title="AI KiCad Copilot API",
    version="1.0.0"
)



# ==========================
# CORS CONFIGURATION
# ==========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],

)



# ==========================
# HEALTH CHECK
# ==========================

@app.get("/")
def home():

    return {

        "status": "running",

        "message": "AI KiCad Copilot Backend"

    }



# ==========================
# GENERATE PROJECT API
# ==========================

@app.post("/api/generate")
async def generate(

    request: GenerateRequest

):


    result = await call_tool(

        "create_kicad_project",

        {

            "project_name":

            "demo_board"

        }

    )


    return {

        "prompt":

        request.prompt,


        "message":

        "KiCad project generated",


        "result":

        str(result)

    }



# ==========================
# TEST MCP TOOL
# ==========================

@app.post("/api/header")
async def create_header():


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

        "message":

        "Header placement generated",


        "result":

        str(result)

    }