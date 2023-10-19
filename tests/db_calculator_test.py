from db_calculator import Calculator
import pytest
from unittest.mock import Mock

# TODO - move test into individual file
@pytest.mark.skip
@pytest.mark.parametrize('number1, number2, result', (
        (4.2, 2.3, 6.5),
        (-3.2, 2.1, -1.1),
        (0.1, 0.2, 0.3)
))
def test_calculator_add_floats(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == pytest.approx(result)
    calculator.remove_results_file()
