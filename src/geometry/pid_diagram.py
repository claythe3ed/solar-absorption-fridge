"""
P&ID for NH3-H2O Solar Absorption Refrigeration Cycle.

Generates a professional process & instrumentation diagram.
Uses matplotlib for fully scriptable, reproducible output.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import os


# ============================================================
# Color scheme
# ============================================================
C_RICH    = '#1f77b4'   # rich solution - blue
C_POOR    = '#d62728'   # poor solution - red
C_VAPOR   = '#2ca02c'   # NH3 vapor - green
C_LIQ     = '#9467bd'   # NH3 liquid - purple
C_HEAT    = '#ff7f0e'   # heat / solar
C_COOL    = '#17becf'   # cooling
C_BORDER  = '#222222'
C_BG      = '#f7f7f7'


# ============================================================
# Component drawing helpers
# ============================================================
def draw_vessel(ax, x, y, w, h, label, tag, color='#e8e8e8'):
    """Draw a vessel (generator, absorber, tank)."""
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=color, edgecolor=C_BORDER, linewidth=1.8, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + 0.05, label, ha='center', va='center',
            fontsize=9, fontweight='bold', zorder=4)
    ax.text(x, y - 0.12, tag, ha='center', va='center',
            fontsize=7, style='italic', color='#444', zorder=4)


def draw_hx(ax, x, y, w, h, label, tag, color='#fff2cc'):
    """Draw heat exchanger (rectangle with diagonal)."""
    box = Rectangle(
        (x - w/2, y - h/2), w, h,
        facecolor=color, edgecolor=C_BORDER, linewidth=1.8, zorder=3)
    ax.add_patch(box)
    # Diagonal line to indicate HX
    ax.plot([x - w/2, x + w/2], [y - h/2, y + h/2],
            color=C_BORDER, linewidth=1.0, zorder=4)
    ax.text(x, y + h/2 + 0.12, label, ha='center', va='bottom',
            fontsize=9, fontweight='bold', zorder=4)
    ax.text(x, y - h/2 - 0.12, tag, ha='center', va='top',
            fontsize=7, style='italic', color='#444', zorder=4)


def draw_cpc(ax, x, y, w, h, label, tag):
    """Draw CPC parabolic collector."""
    # Parabolic curve approximation
    import numpy as np
    xs = np.linspace(-w/2, w/2, 50)
    ys_top = -0.5 * (xs / (w/2))**2 * h + h/2
    ys_bot = -0.5 * (xs / (w/2))**2 * h - h/2
    ax.fill_between(xs + x, ys_bot + y, ys_top + y,
                    color='#fff7d6', edgecolor=C_BORDER, linewidth=1.8, zorder=3)
    # Receiver pipe
    ax.add_patch(Circle((x, y), h*0.18, facecolor='#8b4513',
                         edgecolor=C_BORDER, linewidth=1.5, zorder=4))
    ax.text(x, y + h/2 + 0.15, label, ha='center', va='bottom',
            fontsize=9, fontweight='bold', zorder=5)
    ax.text(x, y - h/2 - 0.15, tag, ha='center', va='top',
            fontsize=7, style='italic', color='#444', zorder=5)


def draw_valve(ax, x, y, label, tag, color=C_BORDER):
    """Draw a generic valve (bowtie)."""
    s = 0.10
    ax.plot([x - s, x, x + s], [y - s, y, y - s],
            color=color, linewidth=1.5, zorder=4)
    ax.plot([x - s, x, x + s], [y + s, y, y + s],
            color=color, linewidth=1.5, zorder=4)
    ax.plot([x, x], [y - s, y + s],
            color=color, linewidth=1.5, zorder=4)
    ax.text(x, y + s + 0.10, label, ha='center', va='bottom',
            fontsize=7, zorder=5)
    ax.text(x, y - s - 0.10, tag, ha='center', va='top',
            fontsize=6, style='italic', color='#444', zorder=5)


def draw_pump(ax, x, y, label, tag):
    """Draw a pump (circle with triangle)."""
    ax.add_patch(Circle((x, y), 0.13, facecolor='#f0f0f0',
                         edgecolor=C_BORDER, linewidth=1.8, zorder=4))
    ax.plot([x - 0.08, x + 0.08, x - 0.08],
            [y + 0.06, y, y - 0.06],
            color=C_BORDER, linewidth=1.5, zorder=5)
    ax.text(x, y - 0.20, label, ha='center', va='top',
            fontsize=7, fontweight='bold', zorder=5)
    ax.text(x, y - 0.32, tag, ha='center', va='top',
            fontsize=6, style='italic', color='#444', zorder=5)


def draw_stream(ax, p1, p2, color, label='', lw=2.0, arrow=True,
                label_offset=(0, 0), style='-'):
    """Draw a process stream (pipe) with optional arrow."""
    if arrow:
        arr = FancyArrowPatch(
            p1, p2, arrowstyle='-|>', mutation_scale=14,
            color=color, linewidth=lw, zorder=2,
            connectionstyle="arc3,rad=0.0", linestyle=style)
        ax.add_patch(arr)
    else:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]],
                color=color, linewidth=lw, zorder=2, linestyle=style)
    if label:
        mx = (p1[0] + p2[0]) / 2 + label_offset[0]
        my = (p1[1] + p2[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, fontsize=7, color=color,
                ha='center', va='center', zorder=5,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                          edgecolor='none', alpha=0.85))


# ============================================================
# Main P&ID
# ============================================================
def build_pid():
    fig, ax = plt.subplots(figsize=(18, 11))
    ax.set_xlim(-0.5, 15.5)
    ax.set_ylim(-0.5, 10.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(7.5, 10.2, 'P&ID — NH$_3$-H$_2$O Solar Absorption Refrigeration Cycle',
            ha='center', fontsize=14, fontweight='bold')
    ax.text(7.5, 9.85, '200 W Cooling · COP = 0.424 · T$_{gen}$ = 135°C · P$_{high}$ = 15.5 bar',
            ha='center', fontsize=9, style='italic', color='#555')

    # ============================================================
    # Equipment placement
    # ============================================================
    # Generator / Solar receiver (top center)
    draw_cpc(ax, 4.0, 8.0, 2.0, 1.0, 'Solar CPC + Generator', 'V-101 / E-101')

    # Condenser (top right)
    draw_hx(ax, 9.5, 7.5, 1.6, 0.9, 'Condenser', 'E-102', color='#d6eaf8')

    # Absorber (bottom left)
    draw_vessel(ax, 3.0, 3.0, 2.0, 1.2, 'Absorber', 'V-102',
                color='#d5f5e3')

    # Solution Heat Exchanger (center)
    draw_hx(ax, 6.0, 5.5, 1.4, 0.8, 'SHX', 'E-103')

    # Evaporator (right bottom)
    draw_hx(ax, 11.0, 3.0, 1.8, 1.0, 'Evaporator\n(cold box)',
            'E-104', color='#e8daef')

    # Rich solution tank
    draw_vessel(ax, 5.0, 1.5, 1.2, 0.8, 'Rich tank', 'V-103',
                color='#aed6f1')

    # Poor solution tank
    draw_vessel(ax, 7.5, 1.5, 1.2, 0.8, 'Poor tank', 'V-104',
                color='#f5b7b1')

    # ============================================================
    # Streams
    # ============================================================

    # --- Rich solution path: Absorber -> SHX -> Generator ---
    # Absorber -> Rich tank
    draw_stream(ax, (3.0, 2.4), (3.0, 1.9), C_RICH, lw=2.2)
    draw_stream(ax, (3.0, 1.9), (4.4, 1.9), C_RICH, lw=2.2)
    # Rich tank -> SHX
    draw_stream(ax, (5.0, 1.9), (5.0, 5.2), C_RICH, lw=2.2)
    draw_stream(ax, (5.0, 5.2), (5.3, 5.5), C_RICH, lw=2.2,
                label='Rich 40%', label_offset=(-0.1, 0.2))
    # SHX -> Generator
    draw_stream(ax, (6.7, 5.6), (8.0, 5.6), C_RICH, lw=2.2)
    draw_stream(ax, (8.0, 5.6), (8.0, 7.5), C_RICH, lw=2.2)
    draw_stream(ax, (8.0, 7.5), (5.0, 7.5), C_RICH, lw=2.2,
                label='to gen', label_offset=(0, 0.15))

    # --- Vapor path: Generator -> Condenser ---
    draw_stream(ax, (5.5, 8.0), (8.7, 8.0), C_VAPOR, lw=2.0,
                label='NH$_3$ vapor (y=0.906)', label_offset=(0, 0.15))
    draw_stream(ax, (8.7, 8.0), (8.7, 7.5), C_VAPOR, lw=2.0)

    # --- Liquid NH3: Condenser -> Evaporator ---
    draw_stream(ax, (9.5, 7.0), (9.5, 6.0), C_LIQ, lw=2.0)
    draw_stream(ax, (9.5, 6.0), (12.5, 6.0), C_LIQ, lw=2.0)
    draw_stream(ax, (12.5, 6.0), (12.5, 3.5), C_LIQ, lw=2.0,
                label='Liquid NH$_3$', label_offset=(0.5, 0))

    # Expansion valve
    draw_valve(ax, 11.5, 6.0, 'Exp. valve', 'VLV-101', color=C_LIQ)

    # --- NH3 vapor: Evaporator -> Absorber ---
    draw_stream(ax, (10.5, 2.5), (8.0, 2.5), C_VAPOR, lw=2.0,
                label='NH$_3$ vapor', label_offset=(0, 0.15))
    draw_stream(ax, (8.0, 2.5), (4.0, 2.5), C_VAPOR, lw=2.0)
    draw_stream(ax, (4.0, 2.5), (4.0, 3.0), C_VAPOR, lw=2.0)

    # --- Poor solution: Generator -> SHX -> Absorber ---
    draw_stream(ax, (4.0, 7.5), (4.0, 6.0), C_POOR, lw=2.0,
                label='Poor 25%', label_offset=(-0.4, 0))
    draw_stream(ax, (4.0, 6.0), (5.3, 6.0), C_POOR, lw=2.0)
    # Through SHX
    draw_stream(ax, (6.7, 6.0), (7.5, 6.0), C_POOR, lw=2.0)
    draw_stream(ax, (7.5, 6.0), (7.5, 1.9), C_POOR, lw=2.0)
    draw_stream(ax, (7.5, 1.9), (3.6, 1.9), C_POOR, lw=2.0)
    draw_stream(ax, (3.6, 1.9), (3.6, 2.4), C_POOR, lw=2.0)

    # Poor solution tank connection
    draw_stream(ax, (7.5, 1.9), (7.5, 1.7), C_POOR, lw=1.5, arrow=False)

    # Throttle valve for poor solution
    draw_valve(ax, 7.5, 4.0, 'Throttle', 'VLV-102', color=C_POOR)

    # ============================================================
    # Sensors and instruments
    # ============================================================
    # Temperature sensor on generator
    ax.add_patch(Circle((5.8, 8.6), 0.10, facecolor='#ffcccc',
                         edgecolor=C_BORDER, linewidth=1.2, zorder=5))
    ax.text(5.8, 8.6, 'T', ha='center', va='center',
            fontsize=8, fontweight='bold', zorder=6)
    ax.text(5.8, 8.85, 'TIC-101', ha='center', fontsize=6, zorder=6)

    # Pressure sensor on condenser
    ax.add_patch(Circle((10.5, 7.5), 0.10, facecolor='#cce5ff',
                         edgecolor=C_BORDER, linewidth=1.2, zorder=5))
    ax.text(10.5, 7.5, 'P', ha='center', va='center',
            fontsize=8, fontweight='bold', zorder=6)
    ax.text(10.5, 7.75, 'PI-102', ha='center', fontsize=6, zorder=6)

    # ============================================================
    # Legend
    # ============================================================
    legend_x = 13.0
    legend_y = 9.0
    ax.text(legend_x, legend_y, 'Legend', fontsize=10, fontweight='bold')
    legend_items = [
        (C_RICH,  'Rich solution (40% NH$_3$)'),
        (C_POOR,  'Poor solution (25% NH$_3$)'),
        (C_VAPOR, 'NH$_3$ vapor'),
        (C_LIQ,   'Liquid NH$_3$'),
        (C_HEAT,  'Heat input'),
        (C_COOL,  'Heat rejection'),
    ]
    for i, (color, text) in enumerate(legend_items):
        y = legend_y - 0.35 - i*0.30
        ax.plot([legend_x, legend_x + 0.4], [y, y],
                color=color, linewidth=3)
        ax.text(legend_x + 0.5, y, text, fontsize=7, va='center')

    # Notes
    notes = (
        'Notes:\n'
        '· V-101 = Generator (solar receiver, 200mm OD, 4m)\n'
        '· V-102 = Absorber (integrated with generator)\n'
        '· E-102 = Condenser (15mm finned, 7.5m)\n'
        '· E-103 = SHX (solution heat exchanger)\n'
        '· E-104 = Evaporator (10mm finned, 6.4m, in cold box)\n'
        '· V-103/V-104 = Solution buffer tanks (3L/2.3L)'
    )
    ax.text(0.0, 0.3, notes, fontsize=7, va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fafafa',
                      edgecolor='#888'))

    plt.tight_layout()
    return fig


# ============================================================
# Save
# ============================================================
if __name__ == "__main__":
    out_dir = '/root/fridge/results/plots'
    os.makedirs(out_dir, exist_ok=True)

    fig = build_pid()
    png_path = os.path.join(out_dir, 'pid_diagram.png')
    pdf_path = os.path.join(out_dir, 'pid_diagram.pdf')

    fig.savefig(png_path, dpi=200, bbox_inches='tight', facecolor='white')
    fig.savefig(pdf_path, bbox_inches='tight', facecolor='white')

    print(f"P&ID saved:")
    print(f"  PNG: {png_path}")
    print(f"  PDF: {pdf_path}")
