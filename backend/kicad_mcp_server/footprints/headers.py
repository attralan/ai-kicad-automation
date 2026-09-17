def create_pin_header(
    pins:int,
    x:float,
    y:float,
    rotation:int = 0
):

    footprint = f"""

(footprint
    "PinHeader_1x{pins}"

    (layer "F.Cu")

    (at {x} {y} {rotation})


    (property "Reference" "J1"
        (at 0 -3 0)
        (layer "F.SilkS")
    )


    (property "Value"
        "PinHeader_{pins}"
        (at 0 3 0)
        (layer "F.Fab")
    )


)

"""

    return footprint