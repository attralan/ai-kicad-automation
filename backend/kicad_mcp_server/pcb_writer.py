def add_footprint(
    pcb_file,
    footprint
):

    with open(
        pcb_file,
        "r"
    ) as file:

        pcb=file.read()


    # Insert before final closing bracket
    position = pcb.rfind(")")


    updated = (
        pcb[:position]
        +
        footprint
        +
        pcb[position:]
    )


    with open(
        pcb_file,
        "w"
    ) as file:

        file.write(updated)


    return pcb_file