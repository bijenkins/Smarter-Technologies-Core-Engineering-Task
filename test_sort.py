import pytest
from sort import sort


def test_standard_package():
    assert sort(10, 10, 10, 5) == "STANDARD"


def test_heavy_package():
    assert sort(10, 10, 10, 25) == "SPECIAL"


def test_bulky_by_volume():
    # 100 * 100 * 100 = 1,000,000
    assert sort(100, 100, 100, 5) == "SPECIAL"


def test_bulky_by_single_dimension():
    assert sort(150, 10, 10, 5) == "SPECIAL"


def test_rejected_heavy_and_bulky():
    assert sort(200, 100, 100, 30) == "REJECTED"


def test_exactly_at_heavy_threshold():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_just_under_heavy_threshold():
    assert sort(10, 10, 10, 19.9) == "STANDARD"


def test_exactly_at_volume_threshold():
    assert sort(100, 100, 100, 10) == "SPECIAL"


def test_just_under_volume_threshold():
    assert sort(99, 100, 100, 10) == "STANDARD"


def test_exactly_at_dimension_threshold():
    assert sort(150, 1, 1, 1) == "SPECIAL"


def test_just_under_dimension_threshold():
    assert sort(149, 1, 1, 1) == "STANDARD"


def test_bulky_volume_and_heavy():
    assert sort(100, 100, 100, 20) == "REJECTED"


def test_bulky_dimension_and_heavy():
    assert sort(150, 1, 1, 20) == "REJECTED"


def test_zero_dimensions():
    assert sort(0, 0, 0, 0) == "STANDARD"


def test_large_but_light():
    assert sort(50, 50, 130, 19) == "STANDARD"


def test_negative_dimension_raises():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 5)


def test_negative_mass_raises():
    with pytest.raises(ValueError):
        sort(10, 10, 10, -5)
