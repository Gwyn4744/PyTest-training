from db_calculator import Calculator
import pytest


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    calculator = Calculator()
    return calculator


def test_calculator_add_integers(calculator):
    calculator = Calculator()
    assert calculator.add(2, 3) == 5


@pytest.mark.skip
def test_calculator_add_integers_skip(calculator):
    calculator = Calculator()
    assert calculator.add(2, 3) == 5


@pytest.mark.skip(reason='any reason')
def test_calculator_add_integers_skip_2(calculator):
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
