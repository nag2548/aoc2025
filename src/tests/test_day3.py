import unittest

from src import day3


class Day3Tests(unittest.TestCase):
    def test_part1(self):
        total = day3.get_total_joltage()
        self.assertEqual(17144, total)


if __name__ == "__main__":
    unittest.main()
