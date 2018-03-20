import unittest

from mydict import MyDict


class TestProcess(unittest.TestCase):
    def setUp(self):
        MyDict.read_file()

    def test_apple(self):
        apples = MyDict.find_word("apple")
        self.assertIn("The wood of the apple tree.", apples)


if __name__ == '__name__':
    unittest.main()
