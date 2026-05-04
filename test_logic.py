import unittest
from logic import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_case_sensitivity(self):
        self.assertTrue(is_palindrome("Radar"))

if __name__ == '__main__':
    unittest.main()
