"""
Ammonia-water mixture properties via Ziegler-Trepp (1984).

Strategy:
- Pure component enthalpies from CoolProp (NIST-accurate)
- Excess enthalpy from Ziegler-Trepp excess Gibbs (E1-E16)
- Bubble/dew temperatures from Patek-Klomfar (1995)
- Vapor composition from activity coefficients

Coefficients cross-validated between:
- Kherris et al. (2013), Thermal Science 17(3):891-902
- Sadhukhan et al., Int. Centre for Applied Thermodynamics 15(3)
- Ziegler & Trepp (1984), Int. J. Refrigeration 7(2):101-106

Units:
- T: Celsius (input), Kelvin (internal)
- P: bar
- x, y: ammonia mass fraction
- h: kJ/kg mixture
"""

import numpy as np
from CoolProp.CoolProp import PropsSI


# ============================================================
# Constants
# ============================================================
R_UNIV = 8.314       # kJ/(kmol·K)
T_B = 100.0          # K
P_B = 10.0           # bar  (Kherris: 10 bar; Sadhukhan: 1 MPa = 10 bar)
M_NH3 = 17.03026     # kg/kmol
M_H2O = 18.01528     # kg/kmol


# ============================================================
# Coefficients (Ziegler-Trepp, Table 1)
# ============================================================
# Ammonia (NH3)
A1_NH3 =  3.971423e-2
A2_NH3 = -1.790557e-5
A3_NH3 = -1.308905e-2
A4_NH3 =  3.752836e-3
B1_NH3 =  1.634519e1
B2_NH3 = -6.508119
B3_NH3 =  1.448937
C1_NH3 = -1.049377e-2
C2_NH3 = -8.288224
C3_NH3 = -6.647257e2
C4_NH3 = -3.045352e3
D1_NH3 =  3.673647
D2_NH3 =  9.989629e-2
D3_NH3 =  3.617622e-2
HLr0_NH3 =  4.878573
HGr0_NH3 = 26.468873
SLr0_NH3 =  1.644773
SGr0_NH3 =  8.339026
Tr0_NH3  =  3.225
Pr0_NH3  =  2.0

# Water (H2O)
A1_H2O =  2.748796e-2
A2_H2O = -1.016665e-5
A3_H2O = -4.452025e-3
A4_H2O =  8.389246e-4
B1_H2O =  1.214557e1
B2_H2O = -1.898065
B3_H2O =  2.911966e-1
C1_H2O =  2.136131e-2
C2_H2O = -3.169291e1
C3_H2O = -4.634611e4
C4_H2O =  0.0
D1_H2O =  4.019170
D2_H2O = -5.175550e-2
D3_H2O =  1.951939e-2
HLr0_H2O = 21.821141
HGr0_H2O = 60.965058
SLr0_H2O =  5.733498
SGr0_H2O = 13.453430
Tr0_H2O  =  5.0705
Pr0_H2O  =  3.0


# ============================================================
# Excess Gibbs coefficients (Kherris Table 2 / Sadhukhan Table II)
# ============================================================
E = np.array([
    -41.733398,   # E1
      0.02414,    # E2
      6.702285,   # E3
     -0.011475,   # E4
     63.608967,   # E5
    -62.490768,   # E6
      1.761064,   # E7
      0.008626,   # E8
      0.387983,   # E9
      0.004772,   # E10
     -4.648107,   # E11
      0.836376,   # E12
     -3.553627,   # E13
      0.000904,   # E14
     24.361723,   # E15
    -20.736547,   # E16
])


# ============================================================
# Patek-Klomfar coefficients (Kherris Table III)
# ============================================================
# m_i, n_i, a_i  for bubble point T_bub(P, x)
PK_BUB = np.array([
    # m, n, a
    [ 0,  0,  0.322302e1],
    [ 0,  1, -0.384206],
    [ 0,  2,  0.460965e-1],
    [ 0,  3, -0.378945e-2],
    [ 0,  4,  0.135610e-3],
    [ 1,  0,  0.487775],
    [ 1,  1, -0.120108],
    [ 1,  2,  0.106154e-1],
    [ 2,  3, -0.533589e-3],
    [ 4,  0,  0.785041e1],
    [ 5,  0, -0.115941e2],
    [ 5,  1, -0.523150e-1],
    [ 6,  0,  0.489596e1],
    [13,  1,  0.421059e-1],
])

# Dew point T_dew(P, y)
PK_DEW = np.array([
    [ 0,  0,  0.324004e1],
    [ 0,  1, -0.395920],
    [ 0,  2,  0.435624e-1],
    [ 0,  3, -0.218943e-2],
    [ 1,  0, -0.143526e1],
    [ 1,  1,  0.105256e1],
    [ 1,  2, -0.719281e-1],
    [ 2,  0,  0.122362e2],
    [ 2,  1, -0.224368e1],
    [ 3,  0, -0.201780e2],
    [ 3,  1,  0.1108344e1],
    [ 4,  0,  0.145399e2],
    [ 4,  2,  0.644312],
    [ 5,  0, -0.221246e1],
    [ 5,  2, -0.756266],
    [ 6,  0, -0.135529e1],
    [ 7,  2,  0.183541],
])


# ============================================================
# Utility functions
# ============================================================
def mass_to_mole(x_mass, M1=M_NH3, M2=M_H2O):
    """Convert NH3 mass fraction to mole fraction."""
    x1 = x_mass / M1
    x2 = (1.0 - x_mass) / M2
    return x1 / (x1 + x2)


def mole_to_mass(x_mole, M1=M_NH3, M2=M_H2O):
    """Convert NH3 mole fraction to mass fraction."""
    m1 = x_mole * M1
    m2 = (1.0 - x_mole) * M2
    return m1 / (m1 + m2)


def _pure_sat_pressure(fluid, T_K):
    """
    Saturation pressure of pure component (bar).
    For T above critical: extrapolate using Clausius-Clapeyron.
    """
    T_crit = PropsSI('Tcrit', fluid)
    P_crit = PropsSI('Pcrit', fluid) / 1e5  # bar

    if T_K < T_crit - 0.5:
        return PropsSI('P', 'T', T_K, 'Q', 0, fluid) / 1e5
    else:
        # Extrapolate above critical (Clausius-Clapeyron, rough)
        # Use saturation pressure at T_crit - 1 K as reference
        T_ref = T_crit - 1.0
        P_ref = PropsSI('P', 'T', T_ref, 'Q', 0, fluid) / 1e5
        # d(ln P)/d(1/T) = -L/R (approximate)
        # Use linear extrapolation in 1/T
        return P_ref * (T_K / T_ref) ** 4.0


def _pure_liquid_h(fluid, T_K):
    """
    Liquid enthalpy (kJ/kg) via CoolProp.
    For T above critical: use compressed fluid at P=100 bar.
    """
    T_crit = PropsSI('Tcrit', fluid)
    if T_K < T_crit - 0.5:
        return PropsSI('H', 'T', T_K, 'Q', 0, fluid) / 1000.0
    else:
        # Above critical: use high-pressure fluid (P=100 bar)
        return PropsSI('H', 'T', T_K, 'P', 100e5, fluid) / 1000.0


def _pure_vapor_h(fluid, T_K):
    """Saturated vapor enthalpy (kJ/kg) via CoolProp."""
    return PropsSI('H', 'T', T_K, 'Q', 1, fluid) / 1000.0


# ============================================================
# Patek-Klomfar: Bubble and Dew Temperatures
# ============================================================
def bubble_temperature(P_bar, x_mass):
    """
    Bubble point temperature in Celsius.
    P in bar, x_mass = NH3 mass fraction.
    """
    P_MPa = P_bar / 10.0  # convert to MPa
    x_mole = mass_to_mole(x_mass)
    ln_ratio = np.log(2.0 / P_MPa)  # P0 = 2 MPa

    T_K = 0.0
    for m_i, n_i, a_i in PK_BUB:
        T_K += a_i * (1.0 - x_mole)**m_i * ln_ratio**n_i
    T_K *= 100.0  # T0 = 100 K
    return T_K - 273.15


def dew_temperature(P_bar, y_mass):
    """
    Dew point temperature in Celsius.
    P in bar, y_mass = NH3 mass fraction in vapor.
    """
    P_MPa = P_bar / 10.0
    y_mole = mass_to_mole(y_mass)
    ln_ratio = np.log(2.0 / P_MPa)

    T_K = 0.0
    for m_i, n_i, a_i in PK_DEW:
        T_K += a_i * (1.0 - y_mole)**m_i * ln_ratio**n_i
    T_K *= 100.0
    return T_K - 273.15


# ============================================================
# Excess Enthalpy (Ziegler-Trepp)
# ============================================================
def excess_enthalpy(T_c, P_bar, x_mole):
    """
    Excess specific enthalpy of liquid mixture (kJ/kmol mixture).
    Computed from Ziegler-Trepp excess Gibbs.
    """
    T_r = (T_c + 273.15) / T_B
    P_r = P_bar / P_B

    # F1, F2, F3 (Eq 12-14)
    F1 = (E[0] + E[1]*P_r + (E[2] + E[3]*P_r)*T_r
          + E[4]/T_r + E[5]/T_r**2)
    F2 = (E[6] + E[7]*P_r + (E[8] + E[9]*P_r)*T_r
          + E[10]/T_r + E[11]/T_r**2)
    F3 = E[12] + E[13]*P_r + E[14]/T_r + E[15]/T_r**2

    # h_E (in reduced units, kJ/kmol when multiplied by R*T_B)
    # h_E / (R*T_B) = -T_r^2 * d(G_r^E/T_r)/dT_r
    term1 = E[0] + E[1]*P_r + 2*E[4]/T_r + 3*E[5]/T_r**2
    term2 = E[6] + E[7]*P_r + 2*E[10]/T_r + 3*E[11]/T_r**2
    term3 = E[12] + E[13]*P_r + 2*E[14]/T_r + 3*E[15]/T_r**2

    h_E_reduced = x_mole * (1 - x_mole) * (
        term1 + (2*x_mole - 1)*term2 + (2*x_mole - 1)**2 * term3
    )
    # Convert to kJ/kmol
    return h_E_reduced * R_UNIV * T_B


# ============================================================
# Activity coefficients from excess Gibbs
# ============================================================
def _g_E_and_dgdx(T_c, P_bar, x_mole):
    """Compute g_E = G_E/(R*T) and dg_E/dx."""
    T_r = (T_c + 273.15) / T_B
    P_r = P_bar / P_B

    F1 = (E[0] + E[1]*P_r + (E[2] + E[3]*P_r)*T_r
          + E[4]/T_r + E[5]/T_r**2)
    F2 = (E[6] + E[7]*P_r + (E[8] + E[9]*P_r)*T_r
          + E[10]/T_r + E[11]/T_r**2)
    F3 = E[12] + E[13]*P_r + E[14]/T_r + E[15]/T_r**2

    W = F1 + F2*(2*x_mole - 1) + F3*(2*x_mole - 1)**2
    dW_dx = 2*F2 + 4*F3*(2*x_mole - 1)

    g_E = (1.0/T_r) * x_mole * (1 - x_mole) * W
    dg_E_dx = (1.0/T_r) * ((1 - 2*x_mole)*W + x_mole*(1 - x_mole)*dW_dx)
    return g_E, dg_E_dx


def activity_coefficients(T_c, P_bar, x_mole):
    """Return ln(gamma_NH3), ln(gamma_H2O)."""
    g_E, dg = _g_E_and_dgdx(T_c, P_bar, x_mole)
    ln_g_nh3 = g_E + (1 - x_mole) * dg
    ln_g_h2o = g_E - x_mole * dg
    return ln_g_nh3, ln_g_h2o


# ============================================================
# Vapor composition from activity model
# ============================================================
def vapor_ammonia_fraction(P_bar, T_c, x_mass):
    """
    NH3 mass fraction in vapor at equilibrium.
    Uses Patek-Klomfar T_bub and activity coefficients.
    """
    x_mole = mass_to_mole(x_mass)
    T_K = T_c + 273.15
    ln_g_nh3, _ = activity_coefficients(T_c, P_bar, x_mole)

    P_sat_nh3 = _pure_sat_pressure('Ammonia', T_K)
    gamma_nh3 = np.exp(ln_g_nh3)

    # Partial pressure of NH3 in vapor phase
    P_nh3 = gamma_nh3 * x_mole * P_sat_nh3

    if P_nh3 >= P_bar:
        return 1.0  # pure NH3 vapor

    y_mole = P_nh3 / P_bar
    return mole_to_mass(y_mole)


# ============================================================
# Mixture enthalpies
# ============================================================
def liquid_enthalpy(T_c, x_mass):
    """
    Saturated liquid mixture enthalpy (kJ/kg mixture).
    h = x*h_NH3 + (1-x)*h_H2O + h_excess
    """
    T_K = T_c + 273.15
    x_mole = mass_to_mole(x_mass)

    # Pure component enthalpies from CoolProp (kJ/kg)
    h_nh3 = _pure_liquid_h('Ammonia', T_K)
    h_h2o = _pure_liquid_h('Water', T_K)

    # Mole fraction mixing on mass basis
    # h_mix = x_mole*h_NH3_molar + (1-x_mole)*h_H2O_molar + h_E_molar
    # Convert to kJ/kg: divide by M_mix = x_mole*M_NH3 + (1-x_mole)*M_H2O
    h_nh3_molar = h_nh3 * M_NH3  # kJ/kmol
    h_h2o_molar = h_h2o * M_H2O  # kJ/kmol

    P_bar = _pure_sat_pressure('Ammonia', T_K) if x_mass > 0.99 else 5.0
    # For estimation of P_r in excess, use partial-pressure-like
    # Use the actual bubble pressure estimate
    # Simple approach: use P_sat_NH3 * x_mole as partial
    P_est = max(_pure_sat_pressure('Ammonia', T_K) * x_mole, 0.5)

    h_E_molar = excess_enthalpy(T_c, P_est, x_mole)  # kJ/kmol mixture

    h_molar = x_mole * h_nh3_molar + (1 - x_mole) * h_h2o_molar + h_E_molar
    M_mix = x_mole * M_NH3 + (1 - x_mole) * M_H2O
    return h_molar / M_mix


def vapor_enthalpy(T_c, y_mass, P_bar=None):
    """
    Superheated vapor mixture enthalpy (kJ/kg mixture).
    Uses partial pressure for each component (real gas behavior).

    T_c: temperature Celsius
    y_mass: NH3 mass fraction in vapor
    P_bar: total pressure (bar). If None, uses pure-component saturation.
    """
    T_K = T_c + 273.15
    y_mole = mass_to_mole(y_mass)

    if P_bar is not None:
        # Partial pressures (bar)
        P_nh3 = y_mole * P_bar
        P_h2o = (1.0 - y_mole) * P_bar

        # Superheated vapor using PT_flash
        h_nh3 = PropsSI('H', 'T', T_K, 'P', P_nh3 * 1e5, 'Ammonia') / 1000.0
        h_h2o = PropsSI('H', 'T', T_K, 'P', P_h2o * 1e5, 'Water') / 1000.0
    else:
        # Fallback: saturated vapor
        h_nh3 = _pure_vapor_h('Ammonia', T_K)
        h_h2o = _pure_vapor_h('Water', T_K)

    h_molar = y_mole * h_nh3 * M_NH3 + (1 - y_mole) * h_h2o * M_H2O
    M_mix = y_mole * M_NH3 + (1 - y_mole) * M_H2O
    return h_molar / M_mix


# ============================================================
# Validation
# ============================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  ZIEGLER-TREPP NH3-H2O PROPERTIES - VALIDATION")
    print("=" * 80)

    print("\n  Test 1: Bubble temperature of PURE ammonia (x=1)")
    print("  Expected: T_sat at 15.5 bar ~= 40 C")
    for P in [5.0, 10.0, 15.5, 20.0]:
        T = bubble_temperature(P, 0.999)
        print(f"    P = {P:>6.2f} bar  ->  T_bub = {T:>7.2f} C")

    print("\n  Test 2: Bubble temperature of PURE water (x=0)")
    print("  Expected: T_sat at 1 bar ~= 100 C")
    for P in [0.5, 1.0, 2.0]:
        T = bubble_temperature(P, 0.001)
        print(f"    P = {P:>6.2f} bar  ->  T_bub = {T:>7.2f} C")

    print("\n  Test 3: Bubble temperature of mixture (x=0.40) at various P")
    for P in [2.4, 5.0, 10.0, 15.5]:
        T = bubble_temperature(P, 0.40)
        print(f"    P = {P:>6.2f} bar, x = 0.40  ->  T_bub = {T:>7.2f} C")

    print("\n  Test 4: Liquid enthalpy of mixture")
    for T, x in [(40, 0.40), (80, 0.40), (120, 0.40),
                 (40, 0.25), (80, 0.25), (120, 0.25)]:
        h = liquid_enthalpy(T, x)
        print(f"    T = {T:>4} C, x = {x:.2f}  ->  h_L = {h:>8.1f} kJ/kg")

    print("\n  Test 5: Vapor fraction at equilibrium")
    for P, T, x in [(2.4, -15, 0.40), (15.5, 120, 0.40),
                    (15.5, 120, 0.25)]:
        y = vapor_ammonia_fraction(P, T, x)
        print(f"    P = {P:>6.2f} bar, T = {T:>5} C, x = {x:.2f}"
              f"  ->  y = {y:.4f}")

    print("\n  Test 6: Vapor enthalpy")
    for T, y in [(40, 0.99), (80, 0.99), (120, 0.99)]:
        h = vapor_enthalpy(T, y)
        print(f"    T = {T:>4} C, y = {y:.2f}  ->  h_G = {h:>8.1f} kJ/kg")

    print("\n" + "=" * 80)


def vapor_ammonia_at_bubble(P_bar, x_mass):
    """
    Vapor NH3 mass fraction at bubble point.
    This is the physically meaningful case for the generator.
    """
    T_bub = bubble_temperature(P_bar, x_mass)
    # At bubble point, use the activity model
    x_mole = mass_to_mole(x_mass)
    T_K = T_bub + 273.15

    ln_g_nh3, ln_g_h2o = activity_coefficients(T_bub, P_bar, x_mole)
    gamma_nh3 = np.exp(ln_g_nh3)
    gamma_h2o = np.exp(ln_g_h2o)

    P_sat_nh3 = _pure_sat_pressure('Ammonia', T_K)
    P_sat_h2o = _pure_sat_pressure('Water', T_K)

    P_partial_nh3 = gamma_nh3 * x_mole * P_sat_nh3
    P_partial_h2o = gamma_h2o * (1 - x_mole) * P_sat_h2o

    P_total = P_partial_nh3 + P_partial_h2o
    if P_total <= 0:
        return None

    y_mole = P_partial_nh3 / P_total
    return mole_to_mass(y_mole)


def y_at_bubble(P_bar, x_mass):
    """Alias for vapor_ammonia_at_bubble."""
    return vapor_ammonia_at_bubble(P_bar, x_mass)
