import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        with self.assertRaises(ZeroDivisionError):  # 测试分母为零
            self.calc.divide(6, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        with self.assertRaises(ZeroDivisionError):  # 测试分母为零
            self.calc.modulo(5, 0)
if __name__ == '__main__':
    unittest.main()
