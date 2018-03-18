import unittest
from fruits import process_fruits


class TestFruits(unittest.TestCase):
    def setUp(self):
        self.fruits = process_fruits()

    def test_apple(self):
        self.assertIn("apple", self.fruits)

    def test_orange(self):
        self.assertIn("orange", self.fruits)
