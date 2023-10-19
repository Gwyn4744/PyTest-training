from db_calculator import Calculator
import pytest


@pytest.fixture(name='calculator')
def fixture_init_calculator(request):
    calculator = Calculator()
    return calculator


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_last_result_verbose(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == result
    assert calculator.last_result_verbose() == f'The last result was {result}.'


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_last_result_verbose_mp(calculator, monkeypatch, number1, number2, result):
    monkeypatch.delattr('db_calculator.Calculator.last_result')
    def last_result_verbose_mock():
        return f'The last result was 6.'
    
    monkeypatch.setattr(calculator, 'last_result_verbose', last_result_verbose_mock)
    assert calculator.add(number1, number2) == result
    assert calculator.last_result_verbose() == f'The last result was 6.'