from db_calculator import Calculator
import pytest
from unittest.mock import Mock


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
    calculator.remove_results_file()


@pytest.mark.parametrize('number1, number2, result', (
        (4.2, 2.3, 6.5),
        (-3.2, 2.1, -1.1),
        (0.1, 0.2, 0.3)
))
def test_calculator_add_floats(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == pytest.approx(result)
    calculator.remove_results_file()


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_get_last_result(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == result
    assert calculator.last_result() == f'{result}'


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_get_last_result_mp(calculator, monkeypatch, number1, number2, result):
    def last_result_mock():
        return result
    
    monkeypatch.setattr(calculator, 'last_result', last_result_mock)
    assert calculator.add(number1, number2) == result
    assert calculator.last_result() == result
