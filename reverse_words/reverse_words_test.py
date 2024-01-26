import unittest
from reverse_words import reverse_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverse_words('apple'), 'elppa')
        self.assertEqual(reverse_words('a b c d'), 'a b c d')
        self.assertEqual(reverse_words(
            'double  spaced  words'), 'elbuod  decaps  sdrow')
