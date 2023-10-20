from db_calculator import Calculator
import pytest
import warnings


# pytestmark = pytest.mark.filterwarnings("ignore::UserWarning:.*filterwarnings.*:")


@pytest.fixture()
def calculator():
    calculator = Calculator()
    app_version_2(calculator.version)
    return calculator


def app_version_2(version):
    if version[0] != 2:
        warnings.warn('This test has been prepared for version 2', UserWarning)
    return version 


@pytest.mark.filterwarnings("ignore")
def test_app_version_2(calculator):
    assert calculator.add(4, 2) == 6


@pytest.mark.filterwarnings("ignore:.*has")
def test_app_version_2_with_message(calculator):
    assert calculator.add(4, 2) == 6


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_app_version_2_with_category(calculator):
    assert calculator.add(4, 2) == 6


@pytest.mark.filterwarnings("ignore:::.*filterwarnings.*:")
def test_app_version_2_with_module(calculator):
    assert calculator.add(4, 2) == 6


@pytest.mark.filterwarnings("ignore::::18")
def test_app_version_2_with_lineno(calculator):
    assert calculator.add(4, 2) == 6
