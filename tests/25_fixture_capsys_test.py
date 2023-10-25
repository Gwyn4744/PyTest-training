from db_calculator import Calculator
import pytest
import sys


# pytest tests/25_fixture_capsys_test.py -vs


# 1

def test_system_echo_1(capsys):
    sys.stderr.write('world\n')
    sys.stdout.write('hello\n')
    captured = capsys.readouterr()
    assert captured.out == 'hello\n'
    assert captured.err == 'world\n'


# 2

def test_system_echo_2(capsys):
    sys.stdout.write('hello\n')
    captured = capsys.readouterr()
    assert captured.out == 'hello\n'
    sys.stdout.write('world\n')
    captured = capsys.readouterr()
    

# 3

def test_system_echo_3(capsys):
    sys.stdout.write('hello\n')
    captured = capsys.readouterr()
    assert captured.out == 'hello\n'
    sys.stdout.write('world\n')
    captured = capsys.readouterr()
    assert captured.out == 'world\n'
    with capsys.disabled():
        sys.stdout.write('Test\n')
    captured = capsys.readouterr()
    with pytest.raises(AssertionError):
        assert captured.out == 'Test\n'
    assert captured.out == ''
    assert captured.err == ''