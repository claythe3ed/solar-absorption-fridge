"""
Test CoolProp ammonia properties against reference values.
"""
from CoolProp.CoolProp import PropsSI

print("=" * 75)
print("  AMMONIA PROPERTIES - CoolProp 8.0.0")
print("=" * 75)
print(f"{'T(C)':>6} {'P_sat(bar)':>12} {'h_fg(kJ/kg)':>14} "
      f"{'rho_liq(kg/m3)':>16} {'rho_vap(kg/m3)':>16}")
print("-" * 75)

for T_c in [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60]:
    T_K = T_c + 273.15
    P = PropsSI('P', 'T', T_K, 'Q', 1, 'Ammonia') / 1e5
    h_vap = PropsSI('H', 'T', T_K, 'Q', 1, 'Ammonia')
    h_liq = PropsSI('H', 'T', T_K, 'Q', 0, 'Ammonia')
    h_fg = (h_vap - h_liq) / 1000
    rho_liq = PropsSI('D', 'T', T_K, 'Q', 0, 'Ammonia')
    rho_vap = PropsSI('D', 'T', T_K, 'Q', 1, 'Ammonia')
    print(f"{T_c:>6} {P:>12.4f} {h_fg:>14.1f} {rho_liq:>16.1f} {rho_vap:>16.4f}")

print("=" * 75)
print()
print("Validation against NIST reference values:")
print("-" * 75)

refs = [
    (-33.3, 1.013, "Triple point ~"),
    (0.0, 4.29, ""),
    (25.0, 10.03, ""),
    (50.0, 20.33, ""),
]

for T_c, P_ref, note in refs:
    T_K = T_c + 273.15
    P_calc = PropsSI('P', 'T', T_K, 'Q', 1, 'Ammonia') / 1e5
    error = (P_calc - P_ref) / P_ref * 100
    print(f"  T = {T_c:>6.1f} C  |  P_ref = {P_ref:>6.3f} bar  |  "
          f"P_calc = {P_calc:>6.3f} bar  |  error = {error:>+6.2f} %  {note}")

print("=" * 75)
