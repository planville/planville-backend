import unittest
from test.TestFidoPhones import TestFidoPhones
from test.TestBellPhones import TestBellPhones
from test.TestVirginPhones import TestVirginPhones
from test.TestRogersPhones import TestRogersPhones

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestBellPhones))
suite.addTests(loader.loadTestsFromTestCase(TestVirginPhones))
suite.addTests(loader.loadTestsFromTestCase(TestFidoPhones))
suite.addTests(loader.loadTestsFromTestCase(TestRogersPhones))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
