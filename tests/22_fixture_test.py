from db_calculator import Calculator
import pytest


# pytest tests/22_fixture_test.py -vs


# 1

# @pytest.fixture
# def calculator():
#     calculator = Calculator()
#     return calculator


# def test_calculator_add_1(calculator):
#     assert calculator.add(2, 3) == 5


# 2 - yield

# @pytest.fixture
# def calculator():
#     calculator = Calculator()
#     print('Code before the test function.')
#     yield calculator
#     print('Code after the test function.')


# def test_calculator_add_1(calculator):
#     print('Test function.')
#     assert calculator.add(2, 3) == 5


# 3 - name parameter 

# @pytest.fixture(name='calculator')
# def fixture_init_calculator():
#     calculator = Calculator()
#     return calculator


# def test_calculator_add_1(calculator):
#     assert calculator.add(2, 3) == 5


# 4 - scope
# 'function' (default), 'class', 'module', 'package', 'session'

# @pytest.fixture(scope='session')
# def calculator():
#     calculator = Calculator()
#     print('Code before the test function.')
#     yield calculator
#     print('Code after the test function.')


# def test_calculator_add_1(calculator):
#     calculator_id = id(calculator)
#     print(f'calculator ID: {calculator_id}')
#     assert calculator.add(2, 3) == 5


# def test_calculator_add_2(calculator):
#     calculator_id = id(calculator)
#     print(f'calculator ID: {calculator_id}')
#     assert calculator.add(2, 3) == 5


# 5 - params parameter 

# @pytest.fixture(name='calculator', params=['no_save', 'save'])
# def fixture_init_calculator(request):
#     if request.param == 'no_save':
#         calculator = Calculator()
#     elif request.param == 'save':
#         calculator = Calculator(save_to_file=True)
#     return calculator


# def test_is_calculator_saves_results(calculator):
#     if calculator.save_to_file == True:
#         assert True
#     else:
#         pytest.skip()


# 6 - autouse
# True, False

# @pytest.fixture(autouse=True, scope='session')
# def calculator_au():
#     print('Fixure with autouse before yield')
#     yield
#     print('Fixure with autouse after yield')


# @pytest.fixture()
# def calculator():
#     calculator = Calculator()
#     print('Code before the test function.')
#     yield calculator
#     print('Code after the test function.')


# def test_calculator_add_1(calculator):
#     calculator_id = id(calculator)
#     print(f'calculator ID: {calculator_id}')
#     assert calculator.add(2, 3) == 5


# def test_calculator_add_2(calculator):
#     calculator_id = id(calculator)
#     print(f'calculator ID: {calculator_id}')
#     assert calculator.add(2, 3) == 5


# 7 - params parameter 

# @pytest.fixture(
#         name='calculator', 
#         params=['no_save', 'save'], 
#         ids=['without saving results', 'with saving results']
#         )
# def fixture_init_calculator(request):
#     if request.param == 'no_save':
#         calculator = Calculator()
#     elif request.param == 'save':
#         calculator = Calculator(save_to_file=True)
#     return calculator


# def test_is_calculator_saves_results(calculator):
#     if calculator.save_to_file == True:
#         assert True
#     else:
#         pytest.skip()
