"""
pressure_vessel_checks.py — ASME BPVC VIII-1 screening formulas for V-101.

STATUS: DRAFT engineering tool, not a certification. Produces a formula-level
screening against UG-27 (shell), UG-32 (2:1 elliptical head), UG-34 (flat
unstayed head), and UG-99 (hydrostatic test) using the material allowable
stresses already on file in docs/COMPONENT_SPECS.md / the Claude project
audit. It does NOT replace a licensed engineer's calculation (see
docs/DESIGN_BASIS.md, DB-01, DB-05) and does NOT decide D-001 (16 vs 25 bar).

Use: import this from cad/scripts/generator.py (or run standalone) to check
whatever geometry is currently hard-coded there, for BOTH open design-pressure
candidates, and get a clear PASS/FAIL instead of silence.

    python3 src/engineering/pressure_vessel_checks.py
"""
import math

# Material allowables used throughout this project's audits (ASME II-D basis).
# Re-confirm against the actual code edition DB-01 selects before use.
S_SHELL_MPA = 118.0   # SA-106 Gr.B, ASME VIII-1 basis
S_CAP_MPA = 138.0     # SA-516 Gr.70
SY_SHELL_MPA = 241.0  # SA-106 Gr.B minimum yield
JOINT_E = 1.0         # seamless shell, full RT on end-cap welds assumed
MILL_UNDERTOL = 0.125 # standard pipe wall under-tolerance (12.5%)

# Both open candidates from docs/DECISION_REGISTER.md D-001. This module does
# not pick one - it reports both until D-001 is resolved.
DESIGN_PRESSURE_CANDIDATES_BAR = (16.0, 25.0)


def shell_required_thickness_mm(od_mm, p_design_bar, corrosion_allow_mm=0.0):
    """UG-27 circumferential stress, thin-wall cylinder."""
    p_mpa = p_design_bar / 10.0
    r = od_mm / 2.0 - corrosion_allow_mm
    return p_mpa * r / (S_SHELL_MPA * JOINT_E - 0.6 * p_mpa) + corrosion_allow_mm


def flat_head_required_thickness_mm(bore_mm, p_design_bar, c=0.33):
    """UG-34(d), flat unstayed circular head. c=0.33 is the typical bolted/
    simple-attachment factor used in the project's earlier screening; a
    specific C depends on the actual edge attachment detail (not yet
    specified anywhere in the repo)."""
    p_mpa = p_design_bar / 10.0
    return bore_mm * math.sqrt(c * p_mpa / (S_CAP_MPA * JOINT_E))


def elliptical_head_required_thickness_mm(bore_mm, p_design_bar):
    """UG-32(d), 2:1 ellipsoidal head."""
    p_mpa = p_design_bar / 10.0
    return (p_mpa * bore_mm) / (2.0 * S_CAP_MPA * JOINT_E - 0.2 * p_mpa)


def hydro_test_pressure_bar(p_design_bar):
    """UG-99(b): 1.3x design pressure, standard hydrostatic test basis."""
    return 1.3 * p_design_bar


def check_generator(od_mm, wall_mm, cap_thick_mm, verbose=True):
    """Check the CURRENT hard-coded V-101 geometry (as read from
    cad/scripts/generator.py) against both open D-001 candidates.
    Returns a list of dicts; does not raise, so a FAIL does not stop CAD
    generation - it is reported so it cannot be silently exported again."""
    t_min_actual = wall_mm * (1.0 - MILL_UNDERTOL)
    bore_mm = od_mm - 2.0 * wall_mm
    results = []
    for p in DESIGN_PRESSURE_CANDIDATES_BAR:
        shell_req = shell_required_thickness_mm(od_mm, p)
        flat_req = flat_head_required_thickness_mm(bore_mm, p)
        ellip_req = elliptical_head_required_thickness_mm(bore_mm, p)
        hydro_req = hydro_test_pressure_bar(p)
        row = {
            "design_pressure_bar": p,
            "shell_ok": t_min_actual >= shell_req,
            "shell_required_mm": round(shell_req, 3),
            "shell_actual_mm": round(t_min_actual, 3),
            "flat_cap_ok": cap_thick_mm >= flat_req,
            "flat_cap_required_mm": round(flat_req, 2),
            "elliptical_cap_required_mm": round(ellip_req, 2),
            "cap_actual_mm": cap_thick_mm,
            "hydro_test_required_bar": round(hydro_req, 1),
        }
        results.append(row)
        if verbose:
            tag = "PASS" if row["shell_ok"] else "FAIL"
            print(f"[{tag}] shell @ {p:.0f} bar: need {row['shell_required_mm']} mm, "
                  f"have {row['shell_actual_mm']} mm")
            tag = "PASS" if row["flat_cap_ok"] else "FAIL"
            print(f"[{tag}] FLAT cap @ {p:.0f} bar: need {row['flat_cap_required_mm']} mm, "
                  f"have {row['cap_actual_mm']} mm "
                  f"(2:1 elliptical alternative would need {row['elliptical_cap_required_mm']} mm)")
            print(f"[INFO] UG-99 hydro test @ {p:.0f} bar design: {row['hydro_test_required_bar']} bar")
    return results


if __name__ == "__main__":
    print("V-101 generator - ASME VIII-1 screening against BOTH open D-001 candidates")
    print("This is a formula-level screening, not a certification (see docs/DESIGN_BASIS.md).")
    print("=" * 78)
    check_generator(od_mm=200.0, wall_mm=2.5, cap_thick_mm=5.0)
