from db_calculator import Calculator
import pytest
import os


@pytest.fixture()
def calculator(request):
    calculator = Calculator()
    return calculator


def test_check_calculator_mode_1(calculator, monkeypatch):
    assert os.environ['CALCULATOR_MODE'] == 'GLOBAL'

    monkeypatch.delenv('CALCULATOR_MODE') 

    with pytest.raises(KeyError): 
        os.environ['CALCULATOR_MODE'] == 'GLOBAL'


def test_check_calculator_mode_2(calculator, monkeypatch):
    assert os.environ['CALCULATOR_MODE'] == 'GLOBAL'

    with pytest.raises(KeyError):
        monkeypatch.delenv('CALCULATOR_MODEE')
        
    monkeypatch.delenv('CALCULATOR_M', raising=False)

    assert os.environ['CALCULATOR_MODE'] == 'GLOBAL'
    