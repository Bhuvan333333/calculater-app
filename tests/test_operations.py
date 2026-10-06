import unittest

from calculator import add, subtract, multiply


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_rejects_zero(self):
        for fn in (add, subtract, multiply):
            with self.assertRaises(ValueError):
                fn(0, 5)

    def test_rejects_negative(self):
        for fn in (add, subtract, multiply):
            with self.assertRaises(ValueError):
                fn(5, -1)

    def test_rejects_non_integer(self):
        for bad in (1.5, "2", None, True):
            for fn in (add, subtract, multiply):
                with self.assertRaises(TypeError):
                    fn(bad, 2)


if __name__ == "__main__":
    unittest.main()
