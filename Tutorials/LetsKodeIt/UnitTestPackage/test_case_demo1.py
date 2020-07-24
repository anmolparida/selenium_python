import unittest


class TestCaseDemo1(unittest.TestCase):

    # def setUpClass(cls):
    #     print('I will run once ')

    def setUp(self):
        print('I will run once before every test')

    def test_methodA(self):
        print('Running Method A')

    def test_methodB(self):
        print('Running method B')

    def tearDown(self):
        print('I will run once after every test')


if __name__ == '__main__':
    unittest.main()

# run from terminal : python -m filename(no extension)
