import pytest


def test_basic():
    assert True


def test_basic_2():
    with pytest.raises(ZeroDivisionError):
        result = 3 / 0