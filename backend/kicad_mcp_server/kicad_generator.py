from pathlib import Path



BASE = Path(
    "../kicad/output"
)



def create_project(name):


    project_folder = BASE / name


    project_folder.mkdir(
        parents=True,
        exist_ok=True
    )


    pcb_file = (
        project_folder /
        f"{name}.kicad_pcb"
    )



    content = f"""

(kicad_pcb

(version 20240108)

(generator pcbnew)


(general

(thickness 1.6)

)


(paper "A4")


(layer

0 "F.Cu"
signal

31 "B.Cu"
signal

36 "B.SilkS"
user

37 "F.SilkS"
user

44 "Edge.Cuts"
user

)


)

"""


    pcb_file.write_text(
        content
    )


    return {


        "status":
        "success",


        "project":
        name,


        "file":
        str(
            pcb_file.resolve()
        )

    }
