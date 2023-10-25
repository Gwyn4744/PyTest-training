from db_calculator import Calculator
import sys


# pytest tests/23_fixture_capfd_test.py -v


# 1

def test_system_echo(capfd):
    sys.stderr.write('world\n')
    sys.stdout.write('hello\n')
    captured = capfd.readouterr()
    assert captured.out == 'hello\n'
    assert captured.err == 'world\n'
