import unittest

from src.days import day5


class Day5Tests(unittest.TestCase):
    def test_part1(self):
        count = day5.count_fresh_ingredients()
        self.assertEqual(640, count)

    def test_part2(self):
        count = day5.count_fresh_ingredients()
        self.assertEqual(3, count)


if __name__ == "__main__":
    unittest.main()
