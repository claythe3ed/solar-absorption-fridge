"""
Ammonia-water absorption refrigeration cycle.
Uses Ziegler-Trepp mixture properties + CoolProp pure components.

State points:
  1  Rich solution leaving absorber (T_abs, x_rich, P_low)
  2  Rich solution entering generator after SHX (T_2, x_rich, P_high)
  3  Vapor leaving generator (T_gen, y_3, P_high)
  4  Poor solution leaving generator (T_gen, x_poor, P_high)
  5  Poor solution entering absorber after SHX+valve (x_poor, P_low)
  6  Liquid NH3 leaving condenser (T_cond, P_high)
  7  Liquid NH3 entering evaporator after valve (T_evap, P_low)
  8  Vapor NH3 leaving evaporator (T_evap, P_low)
"""

import sys
sys.path.insert(0, '/root/fridge/src/thermo')

from CoolProp.CoolProp import PropsSI
from ziegler_trepp_props import (
    bubble_temperature, liquid_enthalpy, vapor_enthalpy,
    vapor_ammonia_at_bubble,
)


# ============================================================
# Design inputs
# ============================================================
DESIGN = {
    "T_evap":     -15.0,   # evaporator temperature (C)
    "T_cond":      40.0,   # condenser temperature (C)
    "T_gen":      135.0,   # generator temperature (C) - for solar
    "T_abs":       30.0,   # absorber temperature (C)
    "Q_evap_W":   200.0,   # cooling load (W)
    "x_rich":       0.40,  # NH3 mass fraction in rich solution
    "x_poor":       0.25,  # NH3 mass fraction in poor solution
    "eta_shx":      0.70,  # solution heat exchanger effectiveness
}


# ============================================================
# CoolProp helpers for pure ammonia
# ============================================================
def nh3_sat_P(T_c, Q):
    """Saturation pressure of pure NH3 (bar)."""
    return PropsSI('P', 'T', T_c + 273.15, 'Q', Q, 'Ammonia') / 1e5


def nh3_h(T_c, Q):
    """Enthalpy of pure NH3 (kJ/kg)."""
    return PropsSI('H', 'T', T_c + 273.15, 'Q', Q, 'Ammonia') / 1000.0


# ============================================================
# Cycle solver
# ============================================================
def solve_cycle(d):
    T_e = d["T_evap"]
    T_c = d["T_cond"]
    T_g = d["T_gen"]
    T_a = d["T_abs"]
    Q_e = d["Q_evap_W"]
    x_r = d["x_rich"]
    x_p = d["x_poor"]
    eta = d["eta_shx"]

    # Pressures
    P_low  = nh3_sat_P(T_e, 1)
    P_high = nh3_sat_P(T_c, 1)

    # Refrigerant path (pure NH3)
    h_6 = nh3_h(T_c, 0)
    h_7 = h_6
    h_8 = nh3_h(T_e, 1)

    # Refrigerant mass flow
    m_r = Q_e / ((h_8 - h_7) * 1000.0)   # kg/s

    # Vapor composition from generator
    y_3 = vapor_ammonia_at_bubble(P_high, x_p)
    h_3 = vapor_enthalpy(T_g, y_3, P_bar=P_high)

    # Solution mass balance
    # m_rich * x_r = m_poor * x_p + m_r * y_3
    # m_rich = m_poor + m_r
    m_poor = m_r * (y_3 - x_r) / (x_r - x_p)
    m_rich = m_poor + m_r
    f = m_rich / m_r

    # State 1: rich solution from absorber
    h_1 = liquid_enthalpy(T_a, x_r)

    # State 4: poor solution from generator
    h_4 = liquid_enthalpy(T_g, x_p)

    # State 2: after SHX (rich side)
    T_2 = T_a + eta * (T_g - T_a)
    h_2 = liquid_enthalpy(T_2, x_r)

    # State 5: poor solution after SHX + valve
    Q_shx = m_rich * (h_2 - h_1)   # kW
    h_5 = h_4 - Q_shx / m_poor

    # Energy balances (kW)
    Q_gen_kW  = m_r * h_3 + m_poor * h_4 - m_rich * h_2
    Q_abs_kW  = m_r * h_8 + m_poor * h_5 - m_rich * h_1
    Q_cond_kW = m_r * (h_3 - h_6)

    # Convert to W
    Q_gen_W  = Q_gen_kW  * 1000.0
    Q_abs_W  = Q_abs_kW  * 1000.0
    Q_cond_W = Q_cond_kW * 1000.0
    Q_shx_W  = Q_shx * 1000.0

    COP = Q_e / Q_gen_W if Q_gen_W > 0 else 0.0

    return {
        "P_low": P_low, "P_high": P_high, "T_2": T_2,
        "h": (h_1, h_2, h_3, h_4, h_5, h_6, h_7, h_8),
        "m_r": m_r, "m_rich": m_rich, "m_poor": m_poor, "f": f,
        "y_3": y_3,
        "Q_evap_W": Q_e, "Q_gen_W": Q_gen_W,
        "Q_abs_W": Q_abs_W, "Q_cond_W": Q_cond_W,
        "Q_shx_W": Q_shx_W, "COP": COP,
    }


# ============================================================
# Pretty print
# ============================================================
def print_results(r, d):
    print("=" * 72)
    print("  NH3-H2O ABSORPTION CYCLE  (Ziegler-Trepp + CoolProp)")
    print("=" * 72)

    print("\n  Design temperatures (C):")
    print(f"    Evaporator:  {d['T_evap']:>8.1f}")
    print(f"    Condenser:   {d['T_cond']:>8.1f}")
    print(f"    Generator:   {d['T_gen']:>8.1f}")
    print(f"    Absorber:    {d['T_abs']:>8.1f}")
    print(f"    SHX outlet:  {r['T_2']:>8.1f}")

    print("\n  Pressures (bar):")
    print(f"    Low:         {r['P_low']:>8.3f}")
    print(f"    High:        {r['P_high']:>8.3f}")
    print(f"    Ratio:       {r['P_high']/r['P_low']:>8.2f}")

    print("\n  Vapor composition at generator:")
    print(f"    y_NH3 = {r['y_3']:.4f}  (mass fraction)")

    print("\n  State enthalpies (kJ/kg):")
    for i, h in enumerate(r['h'], start=1):
        print(f"    h_{i} = {h:>8.1f}")

    print("\n  Mass flows (kg/h):")
    print(f"    Refrigerant:  {r['m_r']*3600:>8.4f}")
    print(f"    Rich sol.:    {r['m_rich']*3600:>8.4f}")
    print(f"    Poor sol.:    {r['m_poor']*3600:>8.4f}")
    print(f"    Circulation f = m_rich/m_r = {r['f']:.2f}")

    print("\n  Energy balance (W):")
    print(f"    Q_evap:      {r['Q_evap_W']:>8.1f}")
    print(f"    Q_gen:       {r['Q_gen_W']:>8.1f}")
    print(f"    Q_abs:       {r['Q_abs_W']:>8.1f}")
    print(f"    Q_cond:      {r['Q_cond_W']:>8.1f}")
    print(f"    Q_shx:       {r['Q_shx_W']:>8.1f}")

    print(f"\n  COP = Q_evap / Q_gen = {r['COP']:.3f}")

    balance = r['Q_evap_W'] + r['Q_gen_W'] - r['Q_abs_W'] - r['Q_cond_W']
    print(f"\n  Energy balance closure: {balance:>+8.2f} W")
    print("=" * 72)


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    result = solve_cycle(DESIGN)
    print_results(result, DESIGN)

    print("\n  DIAGNOSTIC: bubble temperature of solution at P_high")
    print(f"    x_rich = {DESIGN['x_rich']:.2f}"
          f"  ->  T_bub = {bubble_temperature(result['P_high'], DESIGN['x_rich']):>7.2f} C")
    print(f"    x_poor = {DESIGN['x_poor']:.2f}"
          f"  ->  T_bub = {bubble_temperature(result['P_high'], DESIGN['x_poor']):>7.2f} C")
    print(f"    T_gen  = {DESIGN['T_gen']:.2f} C  (must be >= x_poor bubble T)")
