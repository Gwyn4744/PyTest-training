from db_calculator import Calculator
import pytest


# pytest tests/21_mark_xfail_test.py -v


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    calculator = Calculator()
    yield calculator


@pytest.mark.xfail
def test_calculator_add_1(calculator):
    assert calculator.add(2, 3) == 2


@pytest.mark.xfail
def test_calculator_add_2(calculator):
    assert calculator.add(2, 3) == 5


def test_calculator_add_3(calculator):
    if calculator.version[0] < 2:
        pytest.xfail('Old calculatior version.')
    assert calculator.add(2, 3) == 5


@pytest.mark.xfail(reason='Any reason to type.')
def test_calculator_add_4(calculator):
    assert calculator.add(2, 3) == 2


# The first argument is a condition. If Fasle the mark is not
# taken into account
@pytest.mark.xfail(False, reason='Any reason to type.')
def test_calculator_add_5(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.xfail(True, reason='Any reason to type.')
def test_calculator_add_6(calculator):
    assert calculator.add(2, 3) == 2


@pytest.mark.xfail(True, reason='Any reason to type.', raises=AssertionError)
def test_calculator_add_7(calculator):
    assert calculator.add(2, 3) == 2


# @pytest.mark.xfail(True, reason='Any reason to type.', raises=TypeError)
# def test_calculator_add_8(calculator):
#     assert calculator.add(2, 3) == 2


@pytest.mark.xfail(reason='Any reason to type.', run=False)
def test_calculator_add_9(calculator):
    assert calculator.add(2, 3) == 2


@pytest.mark.xfail(strict=True)
def test_calculator_add_10(calculator):
    assert calculator.add(2, 3) == 5


# pytest tests/21_mark_xfail_test.py -vsrx --runxfail


@pytest.mark.parametrize('number1, number2, result', [
        (2, 3, 5),
        pytest.param(2, 3, 2, marks=pytest.mark.xfail(reason="some bug"))
])
def test_calculator_add_11(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result
