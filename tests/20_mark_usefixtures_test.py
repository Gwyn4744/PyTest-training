from db_calculator import Calculator
import pytest


# pytest tests/20_mark_usefixtures_test.py -vs


@pytest.fixture
def set_something():
    print('\nStart')
    yield
    print('End')


# pytestmark = pytest.mark.usefixtures("set_something")


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    print('calculator fixture - start')
    calculator = Calculator()
    yield calculator
    print('calculator fixture - end')


@pytest.mark.usefixtures('set_something')
def test_calculator_add_1(calculator):
    assert calculator.add(2, 3) == 5


def test_calculator_add_2(calculator):
    assert calculator.add(2, 3) == 5