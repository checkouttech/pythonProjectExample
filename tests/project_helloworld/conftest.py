

# place to keep fixtures that are needed by multiple test files 

import pytest

@pytest.fixture
def input_value_from_conftest_fixture():
   input = 39
   return input




