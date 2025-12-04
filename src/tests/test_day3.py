import unittest

from src.days import day3


class Day3Tests(unittest.TestCase):
    def test_part1(self):
        total = day3.get_total_joltage()
        self.assertEqual(17144, total)

    def test_part2(self):
        total = day3.get_total_joltage_2()
        self.assertEqual(170371185255900, total)


if __name__ == "__main__":
    unittest.main()
