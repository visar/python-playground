import unittest
from fruits import process_fruits, fruit_lengths


class TestFruits(unittest.TestCase):
    def setUp(self):
        self.fruits = process_fruits()
        self.lengths = fruit_lengths()

    def test_apple(self):
        self.assertIn("apple", self.fruits)

    def test_orange(self):
        self.assertIn("orange", self.fruits)

    def test_apple_length_in_lengths(self):
        self.assertEqual(len("apple"), self.lengths["apple"])
