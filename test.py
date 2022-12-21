import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
  def test_add(self):
    self.assertEqual(self.calculator.add(8,7), 15)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,2), 8)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(2,7), 14)
  def test_divide(self):
    self.assertEqual(self.calculator.divide(4,2), 2)
  def test_add2(self):
    self.assertEqual(self.calculator.add(2, 2), 5)
if __name__ == "__main__":
  unittest.main()