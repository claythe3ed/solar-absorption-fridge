import pytest


def test_v101_geometry_is_valid_and_connected():
    pytest.importorskip("cadquery")
    from src.geometry.production_cad import build_v101_geometry

    shape = build_v101_geometry().val()
    bounds = shape.BoundingBox()

    assert shape.isValid()
    assert len(shape.Solids()) == 1
    assert bounds.xmin == pytest.approx(-100.0)
    assert bounds.xmax == pytest.approx(160.0)
    assert bounds.ymin == pytest.approx(-100.0)
    assert bounds.ymax == pytest.approx(160.0)
    assert bounds.zmin == pytest.approx(0.0, abs=1e-5)
    assert bounds.zmax == pytest.approx(4000.0)
