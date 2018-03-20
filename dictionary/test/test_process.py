import unittest
from unittest import mock
from mydict import MyDict


class TestProcess(unittest.TestCase):
    def setUp(self):
        MyDict.read_file()

    def test_apple(self):
        apples = MyDict.find_word("apple")
        self.assertIn("The wood of the apple tree.", apples)

    @mock.patch('builtins.input', return_value='Y')
    def test_apples(self, input):
        apples = MyDict.find_word("apples")
        self.assertIn("The wood of the apple tree.", apples)

    @mock.patch('builtins.input', return_value='N')
    def test_nonexisting_apples(self, input):
        apples = MyDict.find_word("apples")
        self.assertEqual("The word doesn't exist", apples)

    def test_nonexisting_word(self):
        match = MyDict.find_word("asdsadasdsadadadasd")
        self.assertEqual("The word doesn't exist", match)


if __name__ == '__name__':
    unittest.main()
