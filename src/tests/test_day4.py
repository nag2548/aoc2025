import unittest

from src import day4 as part1
from src import day4_part2 as part2
from src import day4_part2_variant as part2_variant


class Day4Tests(unittest.TestCase):
    def test_part1(self):
        count = part1.count_rolls()
        self.assertEqual(1409, count)

    def test_part2(self):
        count = part2.count_rolls()
        self.assertEqual(8366, count)

    def test_part2_variant(self):
        count = part2_variant.count_rolls()
        self.assertEqual(8366, count)


if __name__ == "__main__":
    unittest.main()
