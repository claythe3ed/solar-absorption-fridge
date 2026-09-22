"""
Solar collector sizing for the NH3-H2O absorption fridge.

Based on:
- Q_gen from cycle model (471.5 W for baseline design)
- Solar irradiance data (Sudan: ~850 W/m^2 peak)
- Optical and thermal efficiencies
"""

import math


# ============================================================
# Design inputs
# ============================================================
DESIGN = {
    "Q_gen_W":           471.5,   # from cycle_model.py
    "irradiance_Wm2":    850.0,   # Sudan peak (Khoury et al., 2016)
    "optical_eff":       0.75,    # CPC with aluminum mirror + glass
    "thermal_eff":       0.65,    # selective coating + vacuum tube
    "design_margin":     1.40,    # 40% safety margin
    "collector_dia_mm":  200.0,   # receiver pipe diameter
    "acceptance_deg":    30.0,    # CPC acceptance half-angle
}


# ============================================================
# CPC geometry
# ============================================================
def cpc_concentration_ratio(acceptance_half_angle_deg):
    """Max concentration ratio for 2D CPC (ideal)."""
    theta = math.radians(acceptance_half_angle_deg)
    return 1.0 / math.sin(theta)


def cpc_aperture_width(receiver_dia_m, acceptance_deg):
    """Aperture width for CPC."""
    C_max = cpc_concentration_ratio(acceptance_deg)
    return receiver_dia_m * C_max


def required_aperture_area(Q_gen_W, irradiance, eta_opt, eta_thermal, margin):
    """Required mirror aperture area (m^2)."""
    useful_flux = irradiance * eta_opt * eta_thermal
    return (Q_gen_W * margin) / useful_flux


# ============================================================
# Main calculation
# ============================================================
def size_collector(d):
    Q_gen = d["Q_gen_W"]
    G = d["irradiance_Wm2"]
    eta_o = d["optical_eff"]
    eta_t = d["thermal_eff"]
    margin = d["design_margin"]
    D_mm = d["collector_dia_mm"]
    theta = d["acceptance_deg"]

    D_m = D_mm / 1000.0
    aperture_w = cpc_aperture_width(D_m, theta)
    area = required_aperture_area(Q_gen, G, eta_o, eta_t, margin)
    length = area / aperture_w
    C_ratio = aperture_w / D_m

    useful_flux = G * eta_o * eta_t

    print("=" * 72)
    print("  SOLAR COLLECTOR SIZING")
    print("=" * 72)
    print(f"\n  Inputs:")
    print(f"    Q_gen (required):          {Q_gen:>8.1f} W")
    print(f"    Solar irradiance:          {G:>8.1f} W/m^2")
    print(f"    Optical efficiency:        {eta_o*100:>8.1f} %")
    print(f"    Thermal efficiency:        {eta_t*100:>8.1f} %")
    print(f"    Design margin:             {margin:>8.2f} x")
    print(f"    Receiver pipe diameter:    {D_mm:>8.1f} mm")
    print(f"    Acceptance half-angle:     {theta:>8.1f} deg")

    print(f"\n  Derived:")
    print(f"    Useful solar flux:         {useful_flux:>8.1f} W/m^2")
    print(f"    CPC concentration ratio:   {C_ratio:>8.2f}")
    print(f"    Aperture width:            {aperture_w:>8.3f} m")
    print(f"    Aperture area:             {area:>8.3f} m^2")
    print(f"    Collector length:          {length:>8.3f} m")

    print(f"\n  RECOMMENDED SPECIFICATIONS:")
    print(f"    -> Mirror width:           {aperture_w*1000:>6.0f} mm")
    print(f"    -> Mirror length:          {length*1000:>6.0f} mm")
    print(f"    -> Total mirror area:      {area:>8.3f} m^2")
    print(f"    -> Receiver pipe:          {D_mm:>6.0f} mm OD steel")
    print(f"    -> Orientation:            East-West horizontal")
    print(f"    -> Tilt:                   = local latitude (15 deg for Sudan)")
    print("=" * 72)

    return {
        "aperture_width_m": aperture_w,
        "aperture_area_m2": area,
        "length_m": length,
    }


# ============================================================
# Sensitivity analysis
# ============================================================
def sensitivity_analysis(d):
    print("\n" + "=" * 72)
    print("  SENSITIVITY ANALYSIS")
    print("=" * 72)
    print(f"\n  {'Param':<28} {'Value':>10} {'Aperture (m^2)':>18}")
    print("-" * 72)

    base_Q = d["Q_gen_W"]

    # Vary Q_gen
    for mult in [0.5, 0.75, 1.0, 1.25, 1.5]:
        Q = base_Q * mult
        area = required_aperture_area(
            Q, d["irradiance_Wm2"], d["optical_eff"],
            d["thermal_eff"], d["design_margin"])
        print(f"  {'Q_gen = ' + f'{Q:.0f} W':<28} {mult:>10.2f} {area:>18.3f}")

    print()
    # Vary efficiency
    for eta_o in [0.60, 0.70, 0.80]:
        area = required_aperture_area(
            base_Q, d["irradiance_Wm2"], eta_o,
            d["thermal_eff"], d["design_margin"])
        print(f"  {'optical eff = ' + f'{eta_o:.2f}':<28} {eta_o:>10.2f} {area:>18.3f}")

    print()
    # Vary irradiance
    for G in [600, 700, 850, 1000]:
        area = required_aperture_area(
            base_Q, G, d["optical_eff"],
            d["thermal_eff"], d["design_margin"])
        print(f"  {'irradiance = ' + f'{G} W/m2':<28} {G:>10.0f} {area:>18.3f}")

    print("=" * 72)


if __name__ == "__main__":
    result = size_collector(DESIGN)
    sensitivity_analysis(DESIGN)
