"""
Assembly: position all 5 components per P&ID.
Renders the complete solar fridge layout.
"""

import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os


CAD_DIR = "/root/fridge/cad/stl"
OUT_DIR = "/root/fridge/results/plots"


def load(name):
    """Load STL and return mesh."""
    path = os.path.join(CAD_DIR, name)
    m = trimesh.load(path)
    print(f"  Loaded {name}: {len(m.faces)} faces")
    return m


def transform(mesh, translation=(0,0,0), rotation=None, scale=1.0):
    """Apply translation, rotation (euler xyz degrees), scale."""
    m = mesh.copy()
    if scale != 1.0:
        m.apply_scale(scale)
    if rotation is not None:
        from scipy.spatial.transform import Rotation
        R = Rotation.from_euler('xyz', rotation, degrees=True).as_matrix()
        m.apply_transform(np.vstack([np.hstack([R, np.zeros((3,1))]),
                                      [0,0,0,1]]))
    m.apply_translation(translation)
    return m


def render_assembly(meshes, png_path, view=(20, 45)):
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')

    colors = ['steelblue', 'gold', 'crimson', 'seagreen', 'plum']
    alpha = [0.7, 0.5, 0.8, 0.8, 0.6]

    all_pts = []
    for mesh, color, a in zip(meshes, colors, alpha):
        if len(mesh.faces) > 8000:
            idx = np.random.choice(len(mesh.faces), 8000, replace=False)
            tris = mesh.vertices[mesh.faces[idx]]
        else:
            tris = mesh.vertices[mesh.faces]
        coll = Poly3DCollection(tris, alpha=a, facecolor=color,
                                 edgecolor=color, linewidth=0.05)
        ax.add_collection3d(coll)
        all_pts.append(mesh.bounds)

    # Set limits from all meshes
    all_bounds = np.array(all_pts)
    x_min = all_bounds[:,0,0].min()
    x_max = all_bounds[:,1,0].max()
    y_min = all_bounds[:,0,1].min()
    y_max = all_bounds[:,1,1].max()
    z_min = all_bounds[:,0,2].min()
    z_max = all_bounds[:,1,2].max()

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    ax.view_init(elev=view[0], azim=view[1])
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_zlabel('Z (mm)')
    ax.set_title('Assembly — Solar Absorption Fridge (All Components)')

    plt.tight_layout()
    plt.savefig(png_path, dpi=120, bbox_inches='tight')
    plt.close()
    print(f"  Render saved: {png_path}")


# ============================================================
# Positions (based on P&ID layout)
# ============================================================
# Coordinate system: X = width, Y = height, Z = length (4 m axis)

if __name__ == "__main__":
    print("=" * 60)
    print("  BUILDING ASSEMBLY")
    print("=" * 60)

    # 1. Generator (main horizontal, tilted 15° for latitude)
    gen = load("generator.stl")
    gen = transform(gen, translation=(0, 0, 0), rotation=(-15, 0, 0))
    print("  [1/5] Generator positioned")

    # 2. CPC mirror under generator (same tilt)
    cpc = load("cpc_mirror.stl")
    # Mirror sits directly below generator, offset -150 mm in Y
    cpc = transform(cpc, translation=(0, -150, 0), rotation=(-15, 0, 0))
    print("  [2/5] CPC mirror positioned")

    # 3. Condenser (upper right, above generator)
    cond = load("condenser_coil.stl")
    cond = transform(cond, translation=(500, 350, 500))
    print("  [3/5] Condenser positioned")

    # 4. Evaporator (inside cold box, lower right)
    evap = load("evaporator_coil.stl")
    evap = transform(evap, translation=(600, -300, 500))
    print("  [4/5] Evaporator positioned")

    # 5. Cold box (around evaporator)
    box = load("cold_box.stl")
    box = transform(box, translation=(600, -300, 500))
    print("  [5/5] Cold box positioned")

    meshes = [gen, cpc, cond, evap, box]

    print("\nRendering assembly...")
    render_assembly(meshes, os.path.join(OUT_DIR, "assembly_iso.png"),
                    view=(20, 45))
    render_assembly(meshes, os.path.join(OUT_DIR, "assembly_side.png"),
                    view=(0, -90))
    render_assembly(meshes, os.path.join(OUT_DIR, "assembly_top.png"),
                    view=(90, -90))

    print("\n" + "=" * 60)
    print("  ASSEMBLY COMPLETE")
    print("=" * 60)
