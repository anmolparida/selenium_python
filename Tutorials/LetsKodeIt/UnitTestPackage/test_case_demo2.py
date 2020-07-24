import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod  # Decorators or Annotations
    def setUpClass(cls):
        print("*#" * 20)
        print('I will run only once before all tests')
        print("*#" * 20)

    def setUp(self):
        print('I will run once before every test')

    def test_methodA(self):
        print('Running Method A')

    def test_methodB(self):
        print('Running method B')

    def tearDown(self):
        print('I will run once after every test')

    @classmethod
    def tearDownClass(cls):
        print("*#" * 20)
        print('I will run only once after all tests')
        print("*#" * 20)


if __name__ == '__main__':
    unittest.main()

# run from terminal : python -m filename(no extension)
