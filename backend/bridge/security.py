ALLOWED_TOOLS = [

    "create_kicad_project",

    "place_header"

]



def validate_tool(
    name
):


    if name not in ALLOWED_TOOLS:

        raise PermissionError(
            "Tool blocked"
        )


    return True
