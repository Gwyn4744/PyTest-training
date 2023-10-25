from db_calculator import Calculator
import sys


# pytest tests/24_fixture_capfdbinary_test.py -vs


# 1

def test_system_echo(capfdbinary):
    sys.stderr.write('world\n')
    sys.stdout.write('hello\n')
    captured = capfdbinary.readouterr()
    assert captured.out == b'hello\n'
    assert captured.err == b'world\n'
