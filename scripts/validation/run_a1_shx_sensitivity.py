"""
A1 — SHX effectiveness sensitivity study.

Uses the canonical NH3-H2O cycle model and sweeps solution
heat-exchanger effectiveness.

This is a sensitivity study, NOT experimental validation.

Baseline:
    eta_shx = 0.70

Sweep:
    0.16, 0.30, 0.50, 0.70, 0.83

The canonical cycle_model.solve_cycle() API is used directly.
No changes are made to the canonical thermodynamic model.
"""

import csv
import sys
from pathlib import Path

# Repository root
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "thermo"))

from cycle_model import DESIGN, solve_cycle  # noqa: E402


ETA_VALUES = [0.16, 0.30, 0.50, 0.70, 0.83]

OUTPUT = ROOT / "results" / "a1_shx_sensitivity" / "results.csv"


def run_case(eta):
    """Run one SHX-effectiveness sensitivity case."""

    design = DESIGN.copy()
    design["eta_shx"] = eta

    result = solve_cycle(design)

    # Canonical cycle model reports mass flow rates in kg/s.
    # Convert to kg/h for the project's engineering reporting convention.
    m_r_kg_h = result["m_r"] * 3600.0
    m_rich_kg_h = result["m_rich"] * 3600.0
    m_poor_kg_h = result["m_poor"] * 3600.0

    # Overall steady-state cycle closure:
    # Q_evap + Q_gen - Q_abs - Q_cond = 0
    energy_balance_W = (
        result["Q_evap_W"]
        + result["Q_gen_W"]
        - result["Q_abs_W"]
        - result["Q_cond_W"]
    )

    return {
        "eta_shx": eta,
        "Q_evap_W": result["Q_evap_W"],
        "Q_gen_W": result["Q_gen_W"],
        "Q_abs_W": result["Q_abs_W"],
        "Q_cond_W": result["Q_cond_W"],
        "Q_shx_W": result["Q_shx_W"],
        "COP": result["COP"],
        "m_refrigerant_kg_h": m_r_kg_h,
        "m_rich_kg_h": m_rich_kg_h,
        "m_poor_kg_h": m_poor_kg_h,
        "energy_balance_W": energy_balance_W,
    }


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    rows = []

    print("=" * 72)
    print("A1 — SHX EFFECTIVENESS SENSITIVITY")
    print("=" * 72)
    print()
    print(f"Baseline eta_shx = {DESIGN['eta_shx']:.2f}")
    print(f"Sweep = {ETA_VALUES}")
    print()

    for eta in ETA_VALUES:
        row = run_case(eta)
        rows.append(row)

        print(
            f"eta={eta:.2f} | "
            f"Q_evap={row['Q_evap_W']:.2f} W | "
            f"Q_gen={row['Q_gen_W']:.2f} W | "
            f"COP={row['COP']:.4f} | "
            f"closure={row['energy_balance_W']:+.4f} W"
        )

    with OUTPUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print()
    print(f"Results written to: {OUTPUT}")
    print("=" * 72)


if __name__ == "__main__":
    main()
