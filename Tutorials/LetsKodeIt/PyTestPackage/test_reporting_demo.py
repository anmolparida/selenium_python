import pytest
# from LetsKodeIt.PyTestPackage.class_to_test import SomeClassToTest

# run from command line
# py.test -v -s filename.py --html = report.html

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
        assert result == 20
        print('Running method A')

    def test_methodB(self):
        result = self.abc.sumNumbers(3.8,9.5)
        assert result < 20
        print('Running Method B')