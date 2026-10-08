import pytest

from src.thermo.cycle_model import DESIGN, solve_cycle


def test_baseline_cycle_matches_documented_results():
    result = solve_cycle(DESIGN)

    assert result["P_low"] == pytest.approx(2.361, abs=0.001)
    assert result["P_high"] == pytest.approx(15.545, abs=0.001)
    assert result["m_r"] * 3600 == pytest.approx(0.6834, abs=0.001)
    assert result["m_rich"] * 3600 == pytest.approx(2.9882, abs=0.001)
    assert result["m_poor"] * 3600 == pytest.approx(2.3048, abs=0.001)
    assert result["COP"] == pytest.approx(0.424, abs=0.001)

    balance = (result["Q_evap_W"] + result["Q_gen_W"]
               - result["Q_abs_W"] - result["Q_cond_W"])
    assert abs(balance) < 0.01


@pytest.mark.parametrize(
    ("key", "value", "message"),
    [
        ("Q_evap_W", 0, "Q_evap_W must be positive"),
        ("x_poor", DESIGN["x_rich"], "mass fractions"),
        ("x_rich", 1.1, "mass fractions"),
        ("eta_shx", 1.1, "eta_shx"),
        ("T_cond", DESIGN["T_evap"], "T_cond"),
        ("T_gen", DESIGN["T_abs"], "T_gen"),
    ],
)
def test_cycle_rejects_invalid_inputs(key, value, message):
    design = DESIGN.copy()
    design[key] = value

    with pytest.raises(ValueError, match=message):
        solve_cycle(design)


def test_cycle_rejects_non_finite_inputs():
    design = DESIGN.copy()
    design["T_gen"] = float("nan")

    with pytest.raises(ValueError, match="T_gen must be a finite number"):
        solve_cycle(design)


def test_cycle_rejects_generator_below_solution_bubble_temperature():
    design = DESIGN.copy()
    design["T_gen"] = 100.0

    with pytest.raises(ValueError, match="below the poor-solution bubble temperature"):
        solve_cycle(design)