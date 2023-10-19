from db_calculator import Calculator
import pytest


@pytest.fixture(name='calculator')
def fixture_init_calculator(request):
    calculator = Calculator()
    return calculator


def test_cehck_all_last_results(calculator):
    assert calculator.add(4, 2) == 6
    assert calculator.subtract(4, 2) == 2
    assert calculator.multiply(4, 2) == 8
    assert calculator.divide(4, 2) == 2

    my_values = calculator.last_values_dict
    assert my_values['add'] == 6
    assert my_values['subtract'] == 2
    assert my_values['multiply'] == 8
    assert my_values['divide'] == 2


def test_cehck_all_last_results_mp(calculator, monkeypatch):
    assert calculator.add(4, 2) == 6
    assert calculator.subtract(4, 2) == 2
    assert calculator.multiply(4, 2) == 8
    assert calculator.divide(4, 2) == 2

    monkeypatch.setitem(calculator.last_values_dict, 'divide', 0)

    assert calculator.last_values_dict['add'] == 6
    assert calculator.last_values_dict['subtract'] == 2
    assert calculator.last_values_dict['multiply'] == 8
    assert calculator.last_values_dict['divide'] == 0
