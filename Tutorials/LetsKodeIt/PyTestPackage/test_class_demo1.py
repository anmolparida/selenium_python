import pytest
# from LetsKodeIt.PyTestPackage.class_to_test import SomeClassToTest

class SomeClassToTest():

    def __init__(self,value):
        self.value = value

    def sumNumbers(self,a,b):
        return  a + b + self.value



@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 202
        print('Running method A')

    def test_methodB(self):
        print('Running Method B')