from db_calculator import Calculator
import pytest


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_calculator_add_integer(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2, result', (
        (4.2, 2.3, 6.5),
        (-3.2, 2.1, -1.1),
        (0.1, 0.2, 0.3)
))
def test_calculator_add_float(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == pytest.approx(result)