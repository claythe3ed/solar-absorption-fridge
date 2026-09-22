"""
Ammonia-water mixture properties via Soleimani Alamdari (2007).
Simple explicit functions for absorption refrigeration design.

Reference: G. Soleimani Alamdari, "Simple Functions for Predicting the
Thermodynamic Properties of Ammonia-Water Mixture", International Journal
of Engineering, Vol. 20, No. 1, 2007, pp. 94-104.

All temperatures in Celsius.
All pressures in bar.
x = ammonia mass fraction in liquid.
y = ammonia mass fraction in vapor.
h in kJ/kg.
"""

import numpy as np


# ============================================================
# Table 1: Coefficients of Equation 7 (h_L as function of T, x)
# ============================================================
# a_i, b_i, c_i, d_i for i = 0..4
EQ7_A = np.array([-1.8056e-1, -7.2789e-2, -1.2275e-2, +1.6910e-3, -8.1873e-2])
EQ7_B = np.array([+5.3693e0,  -1.2381e-1, +4.1312e-1, -5.0338e-1, +2.0859e-1])
EQ7_C = np.array([-2.0134e-2, +2.2495e-1, -7.4557e-1, +9.9641e-1, -4.6552e-1])
EQ7_D = np.array([+9.8404e-5, -1.1315e-3, +4.1910e-3, -6.1301e-3, +3.1072e-3])


# ============================================================
# Table 3: Coefficients of Equation 9 (P as function of T, x)
# ============================================================
EQ9_A = np.array([+1.2328e0,  -9.9394e0,  +2.6586e1, -1.3512e1])
EQ9_B = np.array([+1.8947e-2, -1.9512e-1, +7.1830e-1, -3.8253e-1])
EQ9_C = np.array([-7.5905e-4, +2.5043e-3, +3.8511e-3, -3.5429e-3])
EQ9_D = np.array([+5.5294e-6, +3.1725e-6, -1.4522e-5, +2.7155e-5])


# ============================================================
# Table 4: Coefficients of Equation 10 (h_G as function of y, P)
# ============================================================
EQ10_A = np.array([+2.6602e-3, -1.1221e-3, -1.5884e-2, -1.2815e-1, -1.4100e-2])
EQ10_B = np.array([-1.2760e-2, +5.4142e-9, -6.4770e-9, -2.7021e-2, -1.8000e-2])
EQ10_C = np.array([0.0,        -5.0529e-20, +5.9400e-20, +1.0632e-3, 0.0])
EQ10_D = np.array([0.0, 0.0, 0.0, -1.3020e-4, 0.0])


# ============================================================
# Table 5: Coefficients of Equation 11 (y as function of x, P)
# ============================================================
EQ11_A = -1.2527e-1
EQ11_B = -2.6700e-1
EQ11_C = -2.2106e-9
EQ11_D = +2.7246e-9


# ============================================================
# Core functions
# ============================================================
def liquid_enthalpy_Tx(T_c, x):
    """Saturated liquid enthalpy (kJ/kg) as function of T (C) and x."""
    h = 0.0
    for i in range(5):
        h += (EQ7_A[i] + EQ7_B[i]*T_c + EQ7_C[i]*T_c**2 + EQ7_D[i]*T_c**3) * x**i
    return h


def saturation_pressure(T_c, x):
    """Saturation (bubble point) pressure (bar) as function of T (C) and x."""
    P = 0.0
    for i in range(4):
        P += (EQ9_A[i] + EQ9_B[i]*T_c + EQ9_C[i]*T_c**2 + EQ9_D[i]*T_c**3) * x**i
    return P


def vapor_enthalpy_yP(y, P_bar):
    """Saturated vapor enthalpy (kJ/kg) as function of y and P (bar)."""
    h = EQ10_A[0] * P_bar**EQ10_B[0]
    for i in range(1, 3):
        h += (EQ10_A[i] + EQ10_B[i]*P_bar + EQ10_C[i]*P_bar**2) * y**i
    # Exponential term
    exp_term = np.exp(EQ10_A[4] * (0.95 - y) * np.exp(EQ10_B[4] * P_bar))
    h += (EQ10_A[3] + EQ10_B[3]*P_bar + EQ10_C[3]*P_bar**2 + EQ10_D[3]*P_bar**3) * exp_term
    return h


def vapor_fraction_y(x, P_bar):
    """Ammonia mass fraction in vapor phase as function of x and P (bar)."""
    return 1.0 - np.exp(EQ11_A * P_bar**EQ11_B * x + (EQ11_C + EQ11_D/P_bar) * x**2)


# ============================================================
# Validation
# ============================================================
if __name__ == "__main__":
    print("=" * 78)
    print("  AMMONIA-WATER PROPERTIES (Soleimani Alamdari 2007)")
    print("=" * 78)

    print("\n  Test 1: Saturation pressure at T=40C, x=0.40")
    P = saturation_pressure(40, 0.40)
    print(f"    P_sat = {P:.4f} bar")
    print(f"    (Expected ~15.5 bar for pure ammonia at 40C;")
    print(f"     for x=0.40, P should be lower)")

    print("\n  Test 2: Liquid enthalpy at T=40C, x=0.40")
    h = liquid_enthalpy_Tx(40, 0.40)
    print(f"    h_L = {h:.1f} kJ/kg")

    print("\n  Test 3: Liquid enthalpy at T=120C, x=0.25")
    h = liquid_enthalpy_Tx(120, 0.25)
    print(f"    h_L = {h:.1f} kJ/kg")

    print("\n  Test 4: Vapor fraction at P=15 bar, x=0.40")
    y = vapor_fraction_y(0.40, 15)
    print(f"    y = {y:.4f} kg NH3 / kg vapor")

    print("\n  Test 5: Vapor enthalpy at P=15 bar, y=0.98")
    h = vapor_enthalpy_yP(0.98, 15)
    print(f"    h_G = {h:.1f} kJ/kg")

    print("\n" + "=" * 78)
