import unittest

from opposite_numbers import opposite_number


class OppositeNumbersTest(unittest.TestCase):
    def test_opposite_number(self):
        self.assertEqual(opposite_number(1), -1)
        self.assertEqual(opposite_number(25.6), -25.6)
        self.assertEqual(opposite_number(0), 0)
        self.assertEqual(opposite_number(1425.2222), -1425.2222)
        self.assertEqual(opposite_number(-3.1458), 3.1458)
        self.assertEqual(opposite_number(-95858588225), 95858588225)
