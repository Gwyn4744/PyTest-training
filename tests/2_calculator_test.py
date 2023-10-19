from db_calculator import Calculator
import pytest


def test_calculator_add_integers():
    calculator = Calculator()
    assert calculator.add(4, 2) == 6