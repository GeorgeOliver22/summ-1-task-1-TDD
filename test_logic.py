import unittest
from logic import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_basic_palindrome(self):
        self.assertTrue(is_palindrome("radar"))

if __name__ == '__main__':
    unittest.main()