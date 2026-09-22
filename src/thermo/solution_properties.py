"""
Ammonia-water solution properties with CoolProp reference state.
"""

from CoolProp.CoolProp import PropsSI


def bubble_pressure(T_c, x_nh3):
    """Bubble point pressure (bar)."""
    log10_Pw = 8.07131 - 1730.63 / (233.426 + T_c)
    Pw = 10.0 ** log10_Pw * 0.00133322
    log10_Pa = 7.36050 - 926.132 / (T_c + 240.170)
    Pa = 10.0 ** log10_Pa * 0.00133322
    return Pw ** (1.0 - x_nh3) * Pa ** x_nh3


def solution_enthalpy(T_c, x_nh3):
    """
    Enthalpy of ammonia-water liquid solution (kJ/kg solution).
    Reference: CoolProp ammonia IIR reference.
    """
    # Pure liquid ammonia enthalpy (CoolProp reference)
    h_nh3 = PropsSI('H', 'T', T_c + 273.15, 'Q', 0, 'Ammonia') / 1000.0
    # Pure liquid water enthalpy (approx, cp=4.18, ref 0C)
    h_h2o = 4.18 * T_c
    # Heat of mixing (exothermic, peak at x=0.4)
    h_mix = -250.0 * x_nh3 * (1.0 - x_nh3) * (1.0 + 0.005 * T_c)
    return (1.0 - x_nh3) * h_h2o + x_nh3 * h_nh3 + h_mix


def vapor_ammonia_fraction(T_c, x_liq):
    """Vapor phase ammonia mass fraction at equilibrium."""
    alpha = 5.0 + 0.05 * T_c
    w = x_liq
    mole_liq = (w / 17.0) / (w / 17.0 + (1.0 - w) / 18.0)
    mole_vap = alpha * mole_liq / (1.0 + (alpha - 1.0) * mole_liq)
    return mole_vap * 17.0 / (mole_vap * 17.0 + (1.0 - mole_vap) * 18.0)


if __name__ == "__main__":
    print(f"{'T(C)':>6} {'x':>6} {'P_bar':>10} {'h_kJ/kg':>12}")
    for T in [40, 80, 120]:
        for x in [0.2, 0.3, 0.4]:
            print(f"{T:>6} {x:>6.2f} {bubble_pressure(T, x):>10.4f} "
                  f"{solution_enthalpy(T, x):>12.1f}")
