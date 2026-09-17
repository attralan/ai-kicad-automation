ALLOWED_TOOLS = [
    "create_kicad_project",

    "create_kicad_schematic",

    "place_header"
]


def check_tool(name):
    if name not in ALLOWED_TOOLS:

        raise Exception(
            "Tool not allowed"
        )
