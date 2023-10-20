from db_calculator import Calculator
import pytest


# pytestmark = pytest.mark.parametrize('number1, number2, result', [
#         (4, 2, 6),
#         (-3, 2, -1),
#         (0, 0, 0)
# ])


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    calculator = Calculator()
    return calculator


@pytest.mark.parametrize('number1, number2, result', [
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
])
def test_calculator_add_integers(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2, result', (
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
))
def test_calculator_add_integers_tuple(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2, result', [
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
])
def test_calculator_add_integers_with_fixture(calculator, number1, number2, result):
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2, result', [
        (4, 2, 6),
        (-3, 2, -1),
        (0, 0, 0)
])
class TestAddOperation:
    def test_calculator_add_integers_1(self, number1, number2, result):
        calculator = Calculator()
        assert calculator.add(number1, number2) == result

    
    def test_calculator_add_integers_2(self, number1, number2, result):
        calculator = Calculator()
        assert calculator.add(number1+1, number2+1) == result+2


@pytest.mark.parametrize('number1, number2', [
        (4, 2),
        (6, 0),
        (12, -6)
])
class TestOperation:
    @pytest.mark.parametrize('number3, result', [
        (6, 0),
        (3, 3),
        (7, -1)
    ])
    def test_calculator(self, calculator, number1, number2, number3, result):
        assert calculator.subtract(calculator.add(number1, number2), number3) == result


@pytest.mark.parametrize('number1, number2, result', [
        (4, 2, 6),
        (-3, 2, -1),
        pytest.param(0, 0, 2, marks=pytest.mark.xfail)
])
def test_calculator_add_integers_with_xfail(number1, number2, result):
    calculator = Calculator()
    assert calculator.add(number1, number2) == result


@pytest.mark.parametrize('number1, number2', [
    (4, 2),
    (6, 0),
    (12, -6)
])
@pytest.mark.parametrize('number3, result', [
    (6, 0),
    (3, 3),
    (7, -1)
])
def test_calculator(calculator, number1, number2, number3, result):
    assert calculator.subtract(calculator.add(number1, number2), number3) == result
