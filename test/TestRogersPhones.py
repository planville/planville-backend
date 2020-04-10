import unittest


class TestRogersPhones(unittest.TestCase):

    @unittest.expectedFailure
    def test_1(self):
        self.assertEqual(8, 9)

    @unittest.expectedFailure
    def test_2(self):
        self.assertEqual(8, 9)

    @unittest.expectedFailure
    def test_3(self):
        self.assertEqual(7, 9)

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(6, 9)

    @unittest.expectedFailure
    def test_5(self):
        self.assertEqual(5, 9)

