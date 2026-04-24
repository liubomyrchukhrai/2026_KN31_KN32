import unittest
# Імпортуємо функції з нашого файлу Calculator.py
from Calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 7), -7)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(10, 0), "Помилка: ділення на нуль!")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(9, 0.5), 3.0)

if __name__ == '__main__':
    unittest.main()