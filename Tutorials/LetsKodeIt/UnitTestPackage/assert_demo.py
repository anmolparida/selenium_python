'''

https://docs.python.org/3/library/unittest.html

'''

import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = False
        self.assertTrue(a, 'a is not True')  # message is displayed if only the test fails
        b = True
        self.assertFalse(b, 'b is not False')  # message is displayed if only the test fails

    def test_assertEqual(self):
        a = 'Test'
        b = 'Testa'
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")  # message is displayed if only the test fails
        self.assertNotEqual(a, b, msg="'a' is equal to 'b")  # message is displayed only if test fails.


if __name__ == '__main__':
    unittest.main(verbosity=2)
