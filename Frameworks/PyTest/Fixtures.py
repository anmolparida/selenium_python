import  pytest

@pytest.fixture
def input_value():
   input_value = 39
   return input_value

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 13== 0