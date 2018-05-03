import unittest
from print1to100 import *

class TestPrint1To100(unittest.TestCase):

	def test_print_1_to_100(self):
		self.assertEqual(print_1_to_100(1), '1')
		self.assertEqual(print_1_to_100(7), '7')
		self.assertEqual(print_1_to_100(9), 'Three')
		self.assertEqual(print_1_to_100(24), 'Three')
		self.assertEqual(print_1_to_100(25), 'Five')
		self.assertEqual(print_1_to_100(85), 'Five')
		self.assertEqual(print_1_to_100(30), 'ThreeFive')
		self.assertEqual(print_1_to_100(75), 'ThreeFive')
		self.assertEqual(print_1_to_100(102), 'Three')
		self.assertEqual(print_1_to_100(888), 'Three')
