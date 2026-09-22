"""
Generator/Solar Receiver 3D model.
Cylinder: 200 mm OD, 2.5 mm wall, 4 m length.
Four ports: vapor out, liquid in, rich in, poor out.
"""

import FreeCAD
import Part
import os


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
out_dir = "/root/fridge/cad"
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
