from db_calculator import Calculator
import sys


# pytest tests/26_fixture_capsysbinary_test.py -vs


# 1

def test_system_echo(capsysbinary):
    sys.stderr.write('world\n')
    sys.stdout.write('hello\n')
    captured = capsysbinary.readouterr()
    assert captured.out == b'hello\n'
    assert captured.err == b'world\n'
