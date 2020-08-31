import pytest

@pytest.fixture
def input_value_from_local_fixture():
   input = 39
   return input

def test_divisible_by_3(input_value_from_local_fixture):
   assert input_value_from_local_fixture % 3 == 0

def test_divisible_by_6(input_value_from_local_fixture):
   assert input_value_from_local_fixture % 6 == 0

def test_divisible_by_6(input_value_from_conftest_fixture):
   assert input_value_from_conftest_fixture % 6 == 0






