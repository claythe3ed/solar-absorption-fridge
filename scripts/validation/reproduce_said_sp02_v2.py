"""
reproduce_said_sp02_v2.py - sensitivity check against Said et al. (2016) SP-02,
using this project's own cycle model. Supersedes reproduce_said_sp02.py.

WHY THIS VERSION EXISTS: the first version set T_gen = 140.0 directly from
Said's reported operating point. Having now read the full primary source
(Design__construction_and_operation_...pdf), that is confirmed wrong, not
just uncertain: the paper's own abstract and nomenclature table define
140/45/-4 as "the temperatures of the generator inlet, the condenser/
absorber inlet and the evaporator outlet" - i.e. the solar-loop HEATING
WATER's inlet temperature to the generator's heating coils, not the
solution/vapor process temperature inside the generator that this project's
T_gen represents (Section 2.2: "heating coils... transfer heat
through the coils into the surrounding solution" - there is necessarily a
temperature drop from the 140C water to the solution it is heating).

So there is no single correct T_gen to plug in from this paper alone - the
paper does not report the internal solution temperature, only the external
HTF inlet. This script sweeps a plausible range of actual generator
temperatures and keeps 140C only as the known upper bound.

Run from the repo root, real venv active (needs CoolProp):
    source venv/bin/activate
    python3 scripts/validation/reproduce_said_sp02_v2.py

STILL APPLIES:
  - x_rich/x_poor/eta_shx below are this project's values, not Said's
    actual solution design. Said's Fig.3 box lists "x_NH3 = 40%" but
    alongside "m_tot = 37 kg" - that reads as the system's overall NH3
    charge fraction, not necessarily the same quantity as this project's
    x_rich. Do not treat the matching "40%" as confirmation they mean the
    same thing.
  - Said's system has a real dephlegmator and diaphragm solution pump;
    this project's model has neither.
  - Said's lowest tested evaporator point in the whole paper is -7C
    (COP 0.30, Table 1). This project's -15C target is colder than every
    point Said reports, and his data trend toward lower COP as evaporator
    temperature drops. That trend, not any single COP comparison, is the
    more defensible takeaway for this project's -15C design point.

This script does not change cycle_model.py and does not close D-007.
"""

import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "..",
        "src",
        "thermo",
    ),
)
from cycle_model import solve_cycle, DESIGN  # noqa: E402


# Said et al. (2016) SP-02 boundary conditions (Table 1, row 2).
HTF_INLET_C = 140.0     # known UPPER BOUND on real generator process temp
T_COND_ABS_C = 45.0
T_EVAP_C = -4.0
Q_EVAP_W = 4500.0
REPORTED_COP = 0.42

# Not from Said et al. These are explicitly swept assumptions representing
# possible HTF-to-process temperature approaches.
APPROACH_SWEEP_K = [5, 10, 15, 20, 25, 30]


def main():
    print("Said et al. (2016) SP-02: sensitivity sweep, not a reproduction.")
    print(f"HTF inlet to generator (known upper bound): {HTF_INLET_C:.0f} C")
    print(f"Said's reported COP at this operating point:  {REPORTED_COP:.2f}")
    print()
    print(
        f"{'Assumed approach (K)':>22} | {'Trial T_gen (C)':>16} | "
        f"{'Model COP':>10} | {'vs Said COP':>12}"
    )
    print("-" * 70)

    for approach in APPROACH_SWEEP_K:
        trial = dict(DESIGN)
        trial.update(
            {
                "T_gen": HTF_INLET_C - approach,
                "T_cond": T_COND_ABS_C,
                "T_abs": T_COND_ABS_C,
                "T_evap": T_EVAP_C,
                "Q_evap_W": Q_EVAP_W,
            }
        )
        try:
            result = solve_cycle(trial)
            cop = result["COP"]
            diff_pct = 100.0 * (cop - REPORTED_COP) / REPORTED_COP
            print(
                f"{approach:>22} | {trial['T_gen']:>16.1f} | "
                f"{cop:>10.4f} | {diff_pct:>+11.1f}%"
            )
        except Exception as exc:
            print(
                f"{approach:>22} | {trial['T_gen']:>16.1f} | "
                f"FAILED: {exc}"
            )

    print()
    print("Read this as a corridor, not a verdict: if the model's COP stays")
    print("close to 0.42 across most of the swept approach range, that is a")
    print("mild positive signal. If it only matches Said at an implausibly")
    print("small or large approach, or never gets close, that is a concrete")
    print("finding to report on issue #1 - either way, state the approach")
    print("values tried, not just a single pass/fail.")
    print()
    print("None of this validates this project's own 0.424 COP at its own")
    print("135/40/-15C design point - that remains a separate, colder")
    print("evaporator condition than anything in Said's tested range.")


if __name__ == "__main__":
    main()
