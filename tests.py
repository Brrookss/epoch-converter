"""Test cases for epoch conversion calculations."""

import unittest

from epoch import converter


class TestCase(unittest.TestCase):

    def test1(self):
        input = 0
        expected = "01-01-1970"
        self.assertEqual(converter(input), expected)

    def test2(self):
        input = 123456789
        expected = "11-29-1973"
        self.assertEqual(converter(input), expected)

    def test3(self):
        input = 9876543210
        expected = "12-22-2282"
        self.assertEqual(converter(input), expected)

    def test4(self):
        input = 2500000000
        expected = "03-22-2049"
        self.assertEqual(converter(input), expected)

    def test5(self):
        input = 201653971200
        expected = "02-29-8360"
        self.assertEqual(converter(input), expected)

    def test6(self):
        input = -1
        with self.assertRaises(ValueError):
            converter(input)


if __name__ == "__main__":
    unittest.main()
