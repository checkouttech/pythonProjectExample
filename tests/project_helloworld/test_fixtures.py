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


@pytest.fixture 
def complex_data():

    class DataTypes(object):
        string = str 
        list = list 
    
    return DataTypes


def test_types(complex_data) :
    assert isinstance("Elephant", complex_data.string ) 
    assert isinstance([5,10,15], complex_data.list ) 


def test_complex_data(complex_data):
    assert isinstance(complex_data, object ) 
    assert complex_data.string == str
    assert complex_data.list == list

