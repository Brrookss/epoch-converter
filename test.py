from epoch_converter import epoch_converter
import unittest


class TestCase(unittest.TestCase):

	def test1(self):
		input_int = 0
		expected_output = '01-01-1970'
		self.assertEqual(epoch_converter(input_int), expected_output)

	def test2(self):
		input_int = 123456789
		expected_output = '11-29-1973'
		self.assertEqual(epoch_converter(input_int), expected_output)

	def test3(self):
		input_int = 9876543210
		expected_output = '12-22-2282'
		self.assertEqual(epoch_converter(input_int), expected_output)

	def test4(self):
		input_int = 201653971200
		expected_output = '02-29-8360'
		self.assertEqual(epoch_converter(input_int), expected_output)

	def test5(self):
		input_int = 2500000000
		expected_output = '03-22-2049'
		self.assertEqual(epoch_converter(input_int), expected_output)


if __name__ == '__main__':
	unittest.main()
