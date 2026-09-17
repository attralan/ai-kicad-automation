from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_DIR = BASE_DIR / "generated_files"


def create_project(name: str):
    folder = OUTPUT_DIR / name

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    pcb_file = folder / f"{name}.kicad_pcb"

    content = """(kicad_pcb
  (version 20240108)
  (generator pcbnew)

  (general
    (thickness 1.6)
  )

  (paper "A4")

  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (44 "Edge.Cuts" user)
  )

  (setup
    (pad_to_mask_clearance 0)
  )

  (net 0 "")
)
"""

    with open(
        pcb_file,
        "w"
    ) as f:
        f.write(content)

    return {
        "status":
        "success",

        "project":
        name,

        "file":
        str(pcb_file)
    }


def create_schematic(name: str):
    """Writes a minimal valid .kicad_sch foundation file (v1.0 target #4)."""
    folder = OUTPUT_DIR / name

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    sch_file = folder / f"{name}.kicad_sch"

    content = """(kicad_sch
  (version 20230121)
  (generator eeschema)

  (paper "A4")

  (title_block
  )

  (lib_symbols
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

    with open(
        sch_file,
        "w"
    ) as f:
        f.write(content)

    return {
        "status":
        "success",

        "project":
        name,

        "file":
        str(sch_file)
    }
