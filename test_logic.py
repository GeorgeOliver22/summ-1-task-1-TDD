import unittest
from logic import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

if __name__ == '__main__':
    unittest.main()

def test_complex_cases(self):
    self.assertTrue(is_palindrome("Radar"))

    