import unittest

from LetsKodeIt.UnitTestPackage.test_class1 import TestClass1
from LetsKodeIt.UnitTestPackage.test_class2 import TestClass2


tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)