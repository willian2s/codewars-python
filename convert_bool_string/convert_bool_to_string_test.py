import unittest
from convert_bool_to_string import boolean_to_string


class TestConvertBoolToString(unittest.TestCase):
    def test_boolean_to_string(self):
        self.assertEqual(boolean_to_string(True), "True")
        self.assertEqual(boolean_to_string(False), "False")
