import unittest
from opposite_attacks import lovefunc


class OppositeAttacksTest(unittest.TestCase):
    def test_opposit_attacks(self):
        self.assertEqual(lovefunc(1, 4), True)
        self.assertEqual(lovefunc(2, 2), False)
        self.assertEqual(lovefunc(0, 1), True)
        self.assertEqual(lovefunc(0, 0), False)
