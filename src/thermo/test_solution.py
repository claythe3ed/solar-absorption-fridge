"""
Test ammonia-water solution properties with CoolProp.
"""
from CoolProp.CoolProp import PropsSI
import numpy as np

print("=" * 75)
print("  AMMONIA-WATER SOLUTION PROPERTIES")
print("=" * 75)
print(f"{'T(C)':>6} {'x_NH3':>8} {'P_bubble(bar)':>16} {'h_mix(kJ/kg)':>16}")
print("-" * 75)

# Ammonia-water mixture
for x in [0.2, 0.3, 0.4, 0.5]:
    for T_c in [20, 40, 60, 80, 100, 120]:
        T_K = T_c + 273.15
        try:
            # Bubble point pressure of ammonia-water mixture
            P = PropsSI('P', 'T', T_K, 'Q', 0, 'AmmoniaWater' if False else 'HEOS::Water[0.5]&Ammonia[0.5]')
            # This is placeholder; real mixture needs REFPROP or specific backend
            # Use individual properties:
            h_liq = PropsSI('H', 'T', T_K, 'Q', 0, 'Ammonia')
            print(f"{T_c:>6} {x:>8.2f} {'N/A':>16} {h_liq/1000:>16.1f}")
        except Exception as e:
            print(f"{T_c:>6} {x:>8.2f}  ERROR: {str(e)[:50]}")
            break
print("=" * 75)
print()
print("Note: Ammonia-water mixture requires REFPROP backend or")
print("      custom mixture model. Pure component data works fine.")
