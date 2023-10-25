from db_calculator import Calculator
import pytest
import sys


# pytest tests/23_fixture_capfd_test.py -v


# 1

# def test_system_echo(capfd):
#     sys.stderr.write('world\n')
#     sys.stdout.write('hello\n')
#     captured = capfd.readouterr()
#     assert captured.out == 'hello\n'
#     assert captured.err == 'world\n'


# 2

def test_system_echo(capfd):
    sys.stdout.write('hello\n')
    captured = capfd.readouterr()
    assert captured.out == 'hello\n'
    sys.stdout.write('world\n')
    captured = capfd.readouterr()
    assert captured.out == 'world\n'
    with capfd.disabled():
        sys.stdout.write('Test\n')
    captured = capfd.readouterr()
    with pytest.raises(AssertionError):
        assert captured.out == 'Test\n'
    assert captured.out == ''
    assert captured.err == ''