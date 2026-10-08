"""
Generator/Solar Receiver 3D model.
Cylinder: 200 mm OD, 2.5 mm wall, 4 m length.
Four ports: vapor out, liquid in, rich in, poor out.

2026-10-05 (Claude): added an ASME screening check before export (see
src/engineering/pressure_vessel_checks.py). This does NOT change OD, WALL,
or CAP_THICK below - those are still the project's existing, unapproved
values. It only makes the existing gap (flat 5mm caps vs. either open
design-pressure candidate, D-001) visible every time this script runs,
instead of silently exporting a STEP file with no warning. Do not raise
CAP_THICK here without a controlled engineering decision (see
docs/DESIGN_BASIS.md, docs/DECISION_REGISTER.md D-001) - this hook is a
check, not a fix.
"""

import FreeCAD
import Part
import os
import sys


# ============================================================
# Parameters (in mm)
# ============================================================
OD = 200.0
WALL = 2.5
LENGTH = 4000.0
ID = OD - 2*WALL

PORT_DIA = 25.0
PORT_PROTRUDE = 40.0
CAP_THICK = 5.0


# ============================================================
# Main hollow cylinder
# ============================================================
outer = Part.makeCylinder(OD/2, LENGTH)
inner = Part.makeCylinder(ID/2, LENGTH)
hollow = outer.cut(inner)

# End caps
cap1 = Part.makeCylinder(OD/2, CAP_THICK)
cap2 = Part.makeCylinder(OD/2, CAP_THICK)
cap2.translate(FreeCAD.Vector(0, 0, LENGTH - CAP_THICK))

body = hollow.fuse(cap1).fuse(cap2)


# ============================================================
# Ports (4 ports)
# ============================================================
def make_port(axis_dir, position):
    """Port stub protruding 40 mm from OUTER surface."""
    stub_len = PORT_PROTRUDE + WALL + 5.0  # overlap into shell
    stub = Part.makeCylinder(PORT_DIA/2, stub_len)
    if axis_dir == "top":
        stub.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0), -90)
        stub.translate(FreeCAD.Vector(0, OD/2 - WALL - 5.0, 0))
    elif axis_dir == "side":
        stub.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0), 90)
        stub.translate(FreeCAD.Vector(OD/2 - WALL - 5.0, 0, 0))
    stub.translate(FreeCAD.Vector(0, 0, position))
    return stub


def make_hole(axis_dir, position):
    """Hole through wall to interior."""
    hole = Part.makeCylinder(PORT_DIA/2, OD + 5.0)
    if axis_dir == "top":
        hole.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0), -90)
        hole.translate(FreeCAD.Vector(0, -OD/2 - 2.5, 0))
    elif axis_dir == "side":
        hole.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0), 90)
        hole.translate(FreeCAD.Vector(-OD/2 - 2.5, 0, 0))
    hole.translate(FreeCAD.Vector(0, 0, position))
    return hole


ports = [
    ("top",  200.0),   # vapor out
    ("top",  3800.0),  # rich in
    ("side", 500.0),   # liquid NH3 in
    ("side", 3500.0),  # poor out
]

body_with_ports = body
for direction, pos in ports:
    stub = make_port(direction, pos)
    hole = make_hole(direction, pos)
    body_with_ports = body_with_ports.fuse(stub)
    body_with_ports = body_with_ports.cut(hole)


# ============================================================
# Export
# ============================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
out_dir = os.path.join(REPO_ROOT, "cad")
os.makedirs(os.path.join(out_dir, "step"), exist_ok=True)
os.makedirs(os.path.join(out_dir, "stl"), exist_ok=True)

step_path = os.path.join(out_dir, "step", "generator.step")
stl_path = os.path.join(out_dir, "stl", "generator.stl")

body_with_ports.exportStep(step_path)
body_with_ports.exportStl(stl_path)

print("=" * 60)
print("GENERATOR MODEL EXPORTED")
print("=" * 60)
print(f"  STEP: {step_path}")
print(f"  STL:  {stl_path}")
print(f"  Volume:    {body_with_ports.Volume/1e6:.3f} L")
print(f"  OD: {OD} mm")
print(f"  ID: {ID} mm")
print(f"  Length: {LENGTH} mm")
print(f"  Ports: {len(ports)}")
bb = body_with_ports.BoundBox
print(f"  Bounding box: {bb.XLength:.0f} x {bb.YLength:.0f} x {bb.ZLength:.0f} mm")
print("=" * 60)

# ============================================================
# ASME screening check (2026-10-05) - reports only, changes nothing above.
# ============================================================
try:
    sys.path.insert(0, os.path.join(REPO_ROOT, "src", "engineering"))
    from pressure_vessel_checks import check_generator
    print("\nASME VIII-1 SCREENING (not a certification - see docs/DESIGN_BASIS.md)")
    print("-" * 60)
    results = check_generator(od_mm=OD, wall_mm=WALL, cap_thick_mm=CAP_THICK)
    if any(not r["flat_cap_ok"] for r in results):
        print("\n*** WARNING: exported STEP uses a flat end cap that FAILS the UG-34 ***")
        print("*** screening at every open D-001 design-pressure candidate. This   ***")
        print("*** export is geometry only - it is not cleared for fabrication.    ***")
    print("-" * 60)
except ImportError as exc:
    print(f"\n[screening skipped: {exc} - run from repo root with "
          f"src/engineering/pressure_vessel_checks.py present]")
