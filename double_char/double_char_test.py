import unittest

from double_char import double_char


class DoubleCharTest(unittest.TestCase):
    def test_double_char(self):
        self.assertEqual(double_char("String"), "SSttrriinngg")
        self.assertEqual(double_char("Hello World"),
                         "HHeelllloo  WWoorrlldd")
        self.assertEqual(double_char("1234!_ "), "11223344!!__  ")
