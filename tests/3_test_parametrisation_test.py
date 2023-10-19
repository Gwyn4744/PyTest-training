from db_calculator import Calculator
import pytest


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_calculator_add_integers(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result