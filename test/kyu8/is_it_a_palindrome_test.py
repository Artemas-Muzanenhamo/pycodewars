import unittest
from solutions.kyu8 import is_palindrome


class MyTestCase(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(is_palindrome.is_palindrome('a'), True)
        self.assertEqual(is_palindrome.is_palindrome('aba'), True)
        self.assertEqual(is_palindrome.is_palindrome('Abba'), True)
        self.assertEqual(is_palindrome.is_palindrome('malam'), True)
        self.assertEqual(is_palindrome.is_palindrome('walter'), False)
        self.assertEqual(is_palindrome.is_palindrome('kodok'), True)
        self.assertEqual(is_palindrome.is_palindrome('Kasue'), False)
