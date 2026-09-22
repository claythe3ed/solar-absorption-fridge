"""
Ammonia-water mixture properties via iapws library (IAPWS-2001).
Wrapper around H2ONH3._prop() that solves for density given T and P.
"""

from iapws.ammonia import H2ONH3
from scipy.optimize import brentq
import numpy as np


class AmmoniaWater:
    """Thermodynamic properties of ammonia-water mixtures (IAPWS-2001)."""

    def __init__(self):
        self._mix = H2ONH3()

    def _residual(self, rho, T_K, P_MPa, x):
        """Pressure residual: P_calc(rho) - P_target."""
        try:
            props = self._mix._prop(rho=rho, T=T_K, x=x)
            return props["P"] - P_MPa
        except Exception:
            return 1e6

    def _solve_rho(self, T_K, P_MPa, x):
        """Find density that matches given T and P."""
        # Bracket: from very low to very high density
        rho_min, rho_max = 0.1, 1200.0

        # Check sign change
        f_min = self._residual(rho_min, T_K, P_MPa, x)
        f_max = self._residual(rho_max, T_K, P_MPa, x)

        if f_min * f_max > 0:
            # Try narrower bracket
            for rho in np.linspace(10, 1000, 100):
                f = self._residual(rho, T_K, P_MPa, x)
                if f * f_min < 0:
                    rho_max = rho
                    break
            else:
                raise ValueError(f"No density solution for T={T_K}, P={P_MPa}, x={x}")

        rho = brentq(self._residual, rho_min, rho_max,
                     args=(T_K, P_MPa, x), xtol=1e-6, maxiter=200)
        return rho

    def properties(self, T_c, P_bar, x_mass):
        """
        Return thermodynamic properties.

        Parameters
        ----------
        T_c : float
            Temperature in Celsius.
        P_bar : float
            Pressure in bar.
        x_mass : float
            Ammonia mass fraction (kg NH3 / kg mixture), 0 to 1.

        Returns
        -------
        dict with keys: h, s, rho, cp, P, T, x_mole
        """
        T_K = T_c + 273.15
        P_MPa = P_bar / 10.0

        # Convert mass fraction to mole fraction
        M_NH3, M_H2O = 17.03026, 18.01528
        x_mole = (x_mass / M_NH3) / (x_mass / M_NH3 + (1 - x_mass) / M_H2O)

        rho = self._solve_rho(T_K, P_MPa, x_mole)
        props = self._mix._prop(rho=rho, T=T_K, x=x_mole)

        return {
            "h": props["h"],
            "s": props["s"],
            "rho": rho,
            "cp": props["cp"],
            "P": props["P"],
            "T": T_K,
            "x_mole": x_mole,
        }


if __name__ == "__main__":
    aw = AmmoniaWater()

    print("=" * 78)
    print("  AMMONIA-WATER MIXTURE PROPERTIES (IAPWS-2001)")
    print("=" * 78)
    print(f"{'T(C)':>6} {'P(bar)':>8} {'x_mass':>8} {'h(kJ/kg)':>12} "
          f"{'rho(kg/m3)':>14} {'cp(kJ/kgK)':>12}")
    print("-" * 78)

    tests = [
        (40, 15, 0.40),
        (40, 15, 0.25),
        (80, 15, 0.40),
        (120, 15, 0.40),
        (120, 15, 0.25),
        (-15, 2.4, 0.999),
    ]

    for T, P, x in tests:
        try:
            r = aw.properties(T, P, x)
            print(f"{T:>6} {P:>8.2f} {x:>8.2f} {r['h']:>12.1f} "
                  f"{r['rho']:>14.1f} {r['cp']:>12.2f}")
        except Exception as e:
            print(f"{T:>6} {P:>8.2f} {x:>8.2f}  ERROR: {str(e)[:40]}")

    print("=" * 78)
