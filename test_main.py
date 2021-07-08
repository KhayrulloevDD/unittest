import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-3, 1), -2)
        self.assertEqual(main.add(-1, -4), -5)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)
        self.assertEqual(main.subtract(-3, 1), -4)
        self.assertEqual(main.subtract(-1, -4), 3)

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        self.assertEqual(main.multiply(-3, 1), -3)
        self.assertEqual(main.multiply(-1, -4), 4)

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(3, -1), -3)
        self.assertEqual(main.divide(-1, -4), 0.25)

        with self.assertRaises(ValueError):
            main.divide(7, 0)


if __name__ == '__main__':
    unittest.main()
