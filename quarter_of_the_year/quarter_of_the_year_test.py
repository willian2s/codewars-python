import unittest

from quarter_of_the_year import quarter_of_the_year


def doTest(test, input, expect):
    actual = quarter_of_the_year(input)
    test.assertEqual(actual, expect, f"Test failed with month = {input}")


class QuarterOfTheYearTest(unittest.TestCase):
    def test_quarter_of_the_year(self):
        doTest(self, 1, 1)
        doTest(self, 2, 1)
        doTest(self, 3, 1)
        doTest(self, 4, 2)
        doTest(self, 5, 2)
        doTest(self, 6, 2)
        doTest(self, 7, 3)
        doTest(self, 8, 3)
        doTest(self, 9, 3)
        doTest(self, 10, 4)
        doTest(self, 11, 4)
        doTest(self, 12, 4)
