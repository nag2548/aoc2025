import unittest

from src import day3 as part1
from src import day3_part2 as part2


class Day3Tests(unittest.TestCase):
    def test_part1(self):
        total = part1.get_total_joltage()
        self.assertEqual(17144, total)

    def test_part2(self):
        total = part2.get_total_joltage()
        self.assertEqual(170371185255900, total)


if __name__ == "__main__":
    unittest.main()
