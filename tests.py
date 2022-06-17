"""Test cases for epoch conversion calculations."""

import unittest

from epoch import converter


class TestCase(unittest.TestCase):

    def testConverter_NegativeInput(self):
        input = -1
        with self.assertRaises(ValueError):
            converter(input)

    def testConverter_MinimumInput(self):
        input = 0
        expected = "01-01-1970"
        self.assertEqual(converter(input), expected)

    def testConverter_SmallInput(self):
        input = 123456789
        expected = "11-29-1973"
        self.assertEqual(converter(input), expected)

    def testConverter_MediumInput(self):
        input = 2500000000
        expected = "03-22-2049"
        self.assertEqual(converter(input), expected)

    def testConverter_LargeInput(self):
        input = 201653971200
        expected = "02-29-8360"
        self.assertEqual(converter(input), expected)


if __name__ == "__main__":
    unittest.main()
