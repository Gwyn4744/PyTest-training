from db_calculator import Calculator
import pytest


# if True:
#     pytest.skip("This is reason.", allow_module_level=True)


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    calculator = Calculator()
    return calculator


def test_calculator_add_integers(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.skip
def test_calculator_add_integers_skip(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.skip(reason='any reason')
def test_calculator_add_integers_skip_2(calculator):
    assert calculator.add(2, 3) == 5



def test_calculator_add_integers_skip_3(calculator):
    if True:
        pytest.skip('any other reason')
    assert calculator.add(2, 3) == 5
