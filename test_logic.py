import unittest
from logic import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_basic_palindrome(self):
        self.assertTrue(is_palindrome("radar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("Manchester"))

    def test_complex_palindromes(self):
        self.assertTrue(is_palindrome("Kayak"))

if __name__ == '__main__':
    unittest.main()
