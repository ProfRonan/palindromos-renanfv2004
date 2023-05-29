"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
from main import is_palindrome  # nopep8 pylint: disable=wrong-import-position


class TestIsPalindrome(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_is_palindrome_empty_string(self):
        """Testa is_palindrome com uma string vazia."""
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_character(self):
        """Tests is_palindrome with a single character string."""
        self.assertTrue(is_palindrome("a"))

    def test_is_palindrome_even_length(self):
        """Tests is_palindrome with an even length string."""
        self.assertTrue(is_palindrome("arara"))
        self.assertFalse(is_palindrome("ola"))

    def test_is_palindrome_odd_length(self):
        """Tests is_palindrome with an odd length string."""
        self.assertTrue(is_palindrome("ovo"))
        self.assertFalse(is_palindrome("mundo"))

    def test_is_palindrome_with_whitespace(self):
        """Tests is_palindrome with a string that contains whitespace."""
        self.assertTrue(is_palindrome("ame o poema"))
        self.assertFalse(is_palindrome("ola mundo"))

    def test_is_palindrome_mixed_case(self):
        """Tests is_palindrome with a mixed case string."""
        self.assertTrue(is_palindrome("Ame o poema"))
        self.assertFalse(is_palindrome("oi mundo"))

    def test_is_palindrome_with_punctuation(self):
        """Tests is_palindrome with a string that contains punctuation."""
        self.assertTrue(is_palindrome("Anotaram a data da maratona!"))
        self.assertFalse(is_palindrome("oi, mundo!"))


if __name__ == "__main__":
    unittest.main()
