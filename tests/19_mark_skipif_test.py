from db_calculator import Calculator
import pytest


# pytestmark = pytest.mark.skipif(True != False, reason='SKIPED ENTIRE MODULE')


# try:
#     from db_calculator3 import Calculator
# except ImportError:
#     db_calculator3 = pytest.importorskip('db_calculator3')


@pytest.fixture(name='calculator')
def fixture_init_calculator():
    calculator = Calculator()
    return calculator


def test_calculator_add_integers(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.skipif
def test_calculator_add_integers_skip(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.skipif(reason='any reason')
def test_calculator_add_integers_skip_2(calculator):
    assert calculator.add(2, 3) == 5



@pytest.mark.skipif(5 < 8, reason='any reason')
def test_calculator_add_integers_skip_3(calculator):
    assert calculator.add(2, 3) == 5


@pytest.mark.skipif(5 > 8, reason='any reason')
def test_calculator_add_integers_skip_4(calculator):
    assert calculator.add(2, 3) == 5


def check_something():
    return 5 > 2


my_skip_condition = pytest.mark.skipif(
    check_something(), reason='just skiped'
)


@my_skip_condition
def test_calculator_add_integers_skip_5(calculator):
    assert calculator.add(2, 3) == 5


@my_skip_condition
class TestAddOperation:
    def test_calculator_add_integers_1(self, calculator):
        assert calculator.add(1, 2) == 3

    
    def test_calculator_add_integers_2(self, calculator):
        assert calculator.add(1, 3) == 4
