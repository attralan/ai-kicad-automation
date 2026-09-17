from kicad_mcp_server.kicad_generator import create_project, create_schematic


def register_tools(mcp):

    @mcp.tool()
    def create_kicad_project(

        project_name: str

    ):

        return create_project(

            project_name

        )

    @mcp.tool()
    def create_kicad_schematic(

        project_name: str

    ):

        return create_schematic(

            project_name

        )

    @mcp.tool()
    def place_header(

        pins: int,

        x_mm: float,

        y_mm: float,

        rotation: int = 0

    ):

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

            rotation

        }
