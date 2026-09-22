"""
Render STL file to PNG for visual verification.
"""
import sys
import os
import numpy as np
import trimesh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def render_stl(stl_path, png_path, view='iso'):
    print(f"Loading: {stl_path}")
    mesh = trimesh.load(stl_path)

    print(f"  Vertices: {len(mesh.vertices)}")
    print(f"  Faces:    {len(mesh.faces)}")
    print(f"  Bounds:   {mesh.bounds}")
    print(f"  Volume:   {mesh.volume/1e6:.3f} L (if closed)")

    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Sample triangles (for speed)
    max_tris = 5000
    faces = mesh.faces
    if len(faces) > max_tris:
        idx = np.random.choice(len(faces), max_tris, replace=False)
        faces = faces[idx]
    triangles = mesh.vertices[faces]

    coll = Poly3DCollection(triangles, alpha=0.5,
                            facecolor='steelblue',
                            edgecolor='navy', linewidth=0.05)
    ax.add_collection3d(coll)

    b = mesh.bounds
    ax.set_xlim(b[0][0], b[1][0])
    ax.set_ylim(b[0][1], b[1][1])
    ax.set_zlim(b[0][2], b[1][2])

    # Set view angle
    if view == 'iso':
        ax.view_init(elev=20, azim=45)
    elif view == 'front':
        ax.view_init(elev=0, azim=-90)
    elif view == 'top':
        ax.view_init(elev=90, azim=-90)

    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_zlabel('Z (mm)')
    ax.set_title(f'Generator 3D Model — {os.path.basename(stl_path)}')

    plt.tight_layout()
    plt.savefig(png_path, dpi=120, bbox_inches='tight')
    plt.close()
    print(f"  Image: {png_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render_stl.py input.stl output.png [view]")
        sys.exit(1)
    view = sys.argv[3] if len(sys.argv) > 3 else 'iso'
    render_stl(sys.argv[1], sys.argv[2], view)
