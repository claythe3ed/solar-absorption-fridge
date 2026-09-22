"""
Mechanical component sizing for the NH3-H2O absorption fridge.

Based on:
- Cycle model outputs (Q_gen, Q_cond, Q_abs, Q_evap)
- Solar collector: 200 mm OD steel pipe, 4 m long
- Household fridge: 150 L box, 200 W cooling
"""

import math


# ============================================================
# Cycle outputs (from cycle_model.py)
# ============================================================
CYCLE = {
    "Q_evap_W":     200.0,
    "Q_gen_W":      471.5,
    "Q_abs_W":      396.7,
    "Q_cond_W":     274.8,
    "Q_shx_W":      277.1,
    "m_r_kg_h":     0.6834,
    "m_rich_kg_h":  2.9882,
    "m_poor_kg_h":  2.3048,
    "T_gen_C":      135.0,
    "T_cond_C":     40.0,
    "T_abs_C":      30.0,
    "T_evap_C":     -15.0,
    "P_high_bar":   15.545,
    "P_low_bar":    2.361,
    "x_rich":       0.40,
    "x_poor":       0.25,
}


# ============================================================
# Physical constants
# ============================================================
RHO_STEEL = 7850      # kg/m^3
RHO_NH3_LIQ = 600     # kg/m^3 at 40 C (approx)
RHO_H2O = 1000        # kg/m^3
SIGMA_YIELD_STEEL = 250e6  # Pa, carbon steel
SAFETY_FACTOR = 4.0


# ============================================================
# 1. GENERATOR (steel receiver tube)
# ============================================================
def size_generator(c, D_mm=200.0, L_m=4.0):
    """
    Generator IS the steel receiver tube in the CPC.
    Must hold rich solution + vapor space.
    """
    D_m = D_mm / 1000.0
    A_cross = math.pi * D_m**2 / 4.0  # m^2

    # Liquid volume: rich solution inventory (say 60% fill)
    # Residence time of ~5 min in generator
    m_solution_kg = c["m_rich_kg_h"] / 60.0 * 5.0  # 5-min inventory
    # Density of rich solution (approx)
    rho_sol = 1.0 / (c["x_rich"] / RHO_NH3_LIQ + (1 - c["x_rich"]) / RHO_H2O)
    V_sol = m_solution_kg / rho_sol

    # Fill level
    fill_frac = 0.30  # 30% liquid, 70% vapor
    V_needed = V_sol / fill_frac
    V_total = A_cross * L_m

    # Wall thickness (Barlow's formula)
    P_pa = c["P_high_bar"] * 1e5
    t_wall_mm = (P_pa * D_m * SAFETY_FACTOR) / (2 * SIGMA_YIELD_STEEL) * 1000

    print("=" * 72)
    print("  GENERATOR / SOLAR RECEIVER")
    print("=" * 72)
    print(f"    OD:                  {D_mm:>8.1f} mm")
    print(f"    Length:              {L_m:>8.3f} m")
    print(f"    Wall thickness:      {t_wall_mm:>8.2f} mm (SF={SAFETY_FACTOR})")
    print(f"    Total volume:        {V_total*1000:>8.2f} L")
    print(f"    Solution inventory:  {m_solution_kg:>8.3f} kg")
    print(f"    Solution volume:     {V_sol*1000:>8.2f} L")
    print(f"    Fill fraction:       {fill_frac*100:>8.0f} %")
    print(f"    Vapor space:         {V_total*(1-fill_frac)*1000:>8.2f} L")
    # Annular cross-section for hollow pipe
    D_inner = D_m - 2*t_wall_mm/1000.0
    A_annular = math.pi * (D_m**2 - D_inner**2) / 4.0
    steel_mass = A_annular * L_m * RHO_STEEL
    print(f"    Steel mass:          {steel_mass:>8.1f} kg (hollow)")
    print("=" * 72)
    return {
        "D_mm": D_mm, "L_m": L_m, "t_wall_mm": t_wall_mm,
        "V_total_L": V_total * 1000, "V_sol_L": V_sol * 1000,
    }


# ============================================================
# 2. CONDENSER
# ============================================================
def size_condenser(c):
    """
    Condenser: finned steel tubes, air-cooled at T_cond = 40 C.
    Heat rejection: Q_cond = 274.8 W
    """
    Q = c["Q_cond_W"]
    dT_approach = 10.0  # K, condenser-to-ambient
    U = 15.0  # W/(m^2*K) for finned tube + natural convection

    A_needed = Q / (U * dT_approach)

    # Use 15 mm OD tubes with fins
    D_tube = 0.015
    fin_factor = 6.0  # finned tube: 6x effective area
    A_actual = A_needed / fin_factor
    L_per_pass = 1.5  # m
    n_passes = math.ceil(A_actual / (math.pi * D_tube * L_per_pass))

    print("=" * 72)
    print("  CONDENSER")
    print("=" * 72)
    print(f"    Heat load:           {Q:>8.1f} W")
    print(f"    Approach dT:         {dT_approach:>8.1f} K")
    print(f"    Overall U:           {U:>8.1f} W/m^2-K")
    print(f"    Area needed:         {A_needed:>8.3f} m^2")
    print(f"    Tube OD:             {D_tube*1000:>8.1f} mm")
    print(f"    Length per pass:     {L_per_pass:>8.1f} m")
    print(f"    Number of passes:    {n_passes:>8.0f}")
    print(f"    Total tube length:   {n_passes*L_per_pass:>8.2f} m")
    print("=" * 72)
    return {"area_m2": A_needed, "n_passes": n_passes}


# ============================================================
# 3. EVAPORATOR
# ============================================================
def size_evaporator(c):
    """
    Evaporator: coil inside insulated 150 L box.
    Q_evap = 200 W, T_evap = -15 C
    """
    Q = c["Q_evap_W"]
    dT = 5.0  # K, air-to-coil
    U = 25.0  # W/(m^2*K), finned air-coil natural convection

    A_needed = Q / (U * dT)
    D_tube = 0.010  # 10 mm OD
    fin_factor = 8.0  # finned tube: 8x effective area
    A_actual = A_needed / fin_factor  # bare tube area needed
    L_coil = A_actual / (math.pi * D_tube)

    print("=" * 72)
    print("  EVAPORATOR")
    print("=" * 72)
    print(f"    Heat load:           {Q:>8.1f} W")
    print(f"    Approach dT:         {dT:>8.1f} K")
    print(f"    Overall U:           {U:>8.1f} W/m^2-K")
    print(f"    Area needed:         {A_needed:>8.3f} m^2")
    print(f"    Tube OD:             {D_tube*1000:>8.1f} mm")
    print(f"    Fin factor:          {fin_factor:>8.1f} x")
    print(f"    Bare tube area:      {A_actual:>8.3f} m^2")
    print(f"    Coil length:         {L_coil:>8.2f} m")
    print(f"    Coil turns (D=300mm):{math.ceil(L_coil/(math.pi*0.3)):>8.0f}")
    print("=" * 72)
    return {"area_m2": A_needed, "L_coil_m": L_coil}


# ============================================================
# 4. ABSORBER
# ============================================================
def size_absorber(c):
    """
    Absorber: same steel cylinder as generator (combined unit),
    OR separate vessel. For continuous cycle, use combined.
    Heat rejection: Q_abs = 396.7 W
    """
    Q = c["Q_abs_W"]
    dT = 5.0  # K, absorber-to-cooling-air
    U = 20.0  # W/(m^2*K), wetted cylinder wall

    A_needed = Q / (U * dT)

    print("=" * 72)
    print("  ABSORBER")
    print("=" * 72)
    print(f"    Heat load:           {Q:>8.1f} W")
    print(f"    Approach dT:         {dT:>8.1f} K")
    print(f"    Overall U:           {U:>8.1f} W/m^2-K")
    print(f"    Area needed:         {A_needed:>8.3f} m^2")
    print(f"    (Can be same vessel as generator)")
    print("=" * 72)
    return {"area_m2": A_needed}


# ============================================================
# 5. SOLUTION TANKS
# ============================================================
def size_solution_tanks(c):
    """Storage for rich and poor solution buffers."""
    # 1-hour operation inventory
    V_rich_L = c["m_rich_kg_h"] * 1.0 / 1.0 * 1.0  # kg / (kg/L)
    V_poor_L = c["m_poor_kg_h"] * 1.0 * 1.0

    print("=" * 72)
    print("  SOLUTION STORAGE TANKS (1-hour buffer)")
    print("=" * 72)
    print(f"    Rich solution:       {V_rich_L:>8.2f} L")
    print(f"    Poor solution:       {V_poor_L:>8.2f} L")
    print("=" * 72)
    return {"V_rich_L": V_rich_L, "V_poor_L": V_poor_L}


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    gen = size_generator(CYCLE)
    print()
    cond = size_condenser(CYCLE)
    print()
    evap = size_evaporator(CYCLE)
    print()
    absb = size_absorber(CYCLE)
    print()
    tanks = size_solution_tanks(CYCLE)

    print("\n" + "=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    print(f"  Generator:   {gen['D_mm']:.0f} mm x {gen['L_m']:.2f} m, "
          f"wall {gen['t_wall_mm']:.1f} mm")
    print(f"  Condenser:   {cond['area_m2']:.3f} m^2 finned steel")
    print(f"  Evaporator:  {evap['L_coil_m']:.2f} m of 10 mm coil")
    print(f"  Absorber:    {absb['area_m2']:.3f} m^2 (same vessel)")
    print(f"  Tanks:       {tanks['V_rich_L']:.1f} L rich, "
          f"{tanks['V_poor_L']:.1f} L poor")
    print("=" * 72)
