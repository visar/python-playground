import unittest
from unittest import mock
from wordfinder import WordFinder


class TestProcess(unittest.TestCase):
    def setUp(self):
        WordFinder.read_file()

    def test_apple(self):
        apples = WordFinder.find_word("apple")
        self.assertIn("The wood of the apple tree.", apples)

    @mock.patch('builtins.input', return_value='Y')
    def test_apples(self, input):
        apples = WordFinder.find_word("apples")
        self.assertIn("The wood of the apple tree.", apples)

    @mock.patch('builtins.input', return_value='N')
    def test_nonexisting_apples(self, input):
        apples = WordFinder.find_word("apples")
        self.assertEqual("The word doesn't exist", apples)

    def test_nonexisting_word(self):
        match = WordFinder.find_word("asdsadasdsadadadasd")
        self.assertEqual("The word doesn't exist", match)

    def test_texas_lower(self):
        texas = WordFinder.find_word("texas")
        self.assertIn(
            "The 28th state of the United States of America, "
            "located in the southern US.",
            texas)

    def test_texas_upper(self):
        texas = WordFinder.find_word("TEXAS")
        self.assertIn(
            "The 28th state of the United States of America, "
            "located in the southern US.",
            texas)

    def test_texas_mixed(self):
        texas = WordFinder.find_word("tExAs")
        self.assertIn(
            "The 28th state of the United States of America, "
            "located in the southern US.",
            texas)


if __name__ == '__name__':
    unittest.main()
