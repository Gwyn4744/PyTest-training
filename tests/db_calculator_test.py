from db_calculator import Calculator
import pytest


@pytest.fixture(name='calculator', params=['no_save', 'save'])
def fixture_init_calculator(request):
    if request.param == 'no_save':
        calculator = Calculator()
    elif request.param == 'save':
        calculator = Calculator(save_to_file=True)
    return calculator


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_calculator_add_integers(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2, result', (
        (4.2, 2.3, 6.5),
        (-3.2, 2.1, -1.1),
        (0.1, 0.2, 0.3)
))
def test_calculator_add_floats(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == pytest.approx(result)