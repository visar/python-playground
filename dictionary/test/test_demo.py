import unittest


class TestDemo(unittest.TestCase):
    def setUp(self):
        pass

    def test_demo(self):
        self.assertEqual(1, 1)


if __name__ == '__name__':
    unittest.main()
