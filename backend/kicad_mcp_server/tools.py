import sys
import os


# Add current folder to Python path
CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

sys.path.append(
    CURRENT_DIR
)


from kicad_generator import create_project



def register_tools(mcp):


    @mcp.tool()
    def create_kicad_project(
        project_name: str
    ):

        """
        Generate a KiCad PCB project.
        """

        return create_project(
            project_name
        )



    @mcp.tool()
    def place_header(
        pins: int,
        x_mm: float,
        y_mm: float,
        rotation: int = 0
    ):

        """
        Create a pin header placement command.
        """


        if pins not in [
            2,
            3,
            4,
            5,
            6,
            8,
            10
        ]:

            return {

                "error":
                "Unsupported header size"

            }



        return {

            "component":
            "PinHeader",


            "pins":
            pins,


            "position":
            {

                "x_mm":
                x_mm,


                "y_mm":
                y_mm

            },


            "rotation":
            rotation,


            "status":
            "preview_only"

        }