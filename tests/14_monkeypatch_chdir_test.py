from db_calculator import Calculator
import pytest
import os


@pytest.fixture()
def calculator():
    calculator = Calculator()
    return calculator


def test_chdir_1(calculator, monkeypatch):
    new_dir = '/home/dominik/Desktop/PyTest-Training/tests'
    old_dir = os.getcwd()

    monkeypatch.chdir(new_dir)

    current_dir = os.getcwd()

    assert current_dir == new_dir
    assert current_dir != old_dir
