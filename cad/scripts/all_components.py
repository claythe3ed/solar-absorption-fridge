"""Build remaining components with controlled mesh."""

import FreeCAD
import Part
import Mesh
import os


OUT_STEP = "/root/fridge/cad/step"
OUT_STL = "/root/fridge/cad/stl"
os.makedirs(OUT_STEP, exist_ok=True)
os.makedirs(OUT_STL, exist_ok=True)


def export_coarse(shape, name, tol=2.0):
    """Export STEP + coarse STL."""
    step_path = os.path.join(OUT_STEP, name + ".step")
    stl_path  = os.path.join(OUT_STL, name + ".stl")

    shape.exportStep(step_path)

    # Tessellate with tolerance, then write mesh
    verts, facets = shape.tessellate(tol)
    mesh = Mesh.Mesh()
    for f in facets:
        mesh.addFacet(verts[f[0]], verts[f[1]], verts[f[2]])
    mesh.write(stl_path)

    size_kb = os.path.getsize(stl_path) / 1024
    print("  " + name + ": Vol=" + str(round(shape.Volume/1e6, 3))
          + " L, STL=" + str(round(size_kb, 1)) + " KB, "
          + "facets=" + str(len(facets)))


def make_coil_simple(tube_od, coil_dia, turns, pitch=100.0):
    tube_r = tube_od / 2
    coil_r = coil_dia / 2
    tori = []
    for i in range(turns):
        z = i * pitch
        t = Part.makeTorus(coil_r, tube_r,
                            FreeCAD.Vector(0, 0, z),
                            FreeCAD.Vector(0, 0, 1))
        tori.append(t)
    return Part.makeCompound(tori)


def make_cold_box():
    inner = Part.makeBox(500, 500, 600)
    outer = Part.makeBox(700, 700, 800)
    outer.translate(FreeCAD.Vector(-100, -100, -100))
    return outer.cut(inner)


print("=" * 60)
print("  BUILDING REMAINING COMPONENTS")
print("=" * 60)

print("[1/3] Condenser (5 tori, 15 mm)...")
export_coarse(make_coil_simple(15.0, 300.0, 5), "condenser_coil")

print("[2/3] Evaporator (7 tori, 10 mm)...")
export_coarse(make_coil_simple(10.0, 300.0, 7), "evaporator_coil")

print("[3/3] Cold box...")
export_coarse(make_cold_box(), "cold_box")

print("=" * 60)
print("  DONE")
print("=" * 60)
