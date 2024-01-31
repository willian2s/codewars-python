import unittest

from grade_book import get_grade


class GradeBookTest(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual(get_grade(95, 90, 93), 'A')
        self.assertEqual(get_grade(70, 70, 100), 'B')
        self.assertEqual(get_grade(70, 70, 70), 'C')
        self.assertEqual(get_grade(50, 50, 95), 'D')
        self.assertEqual(get_grade(0, 0, 5), 'F')
