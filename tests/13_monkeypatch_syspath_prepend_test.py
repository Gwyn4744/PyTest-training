from db_calculator import Calculator
import pytest
import sys


@pytest.fixture()
def calculator():
    calculator = Calculator()
    return calculator


def test_add_syspath_1(calculator, monkeypatch):
    new_path = '/home/dominik/Desktop/PyTest-Training/test'

    monkeypatch.syspath_prepend(new_path) 

    assert sys.path[0] == new_path
