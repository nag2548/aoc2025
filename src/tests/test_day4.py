import unittest

from src.days import day4


class Day4Tests(unittest.TestCase):
    def test_part1(self):
        count = day4.count_rolls()
        self.assertEqual(1409, count)

    def test_part2(self):
        count = day4.count_rolls_2()
        self.assertEqual(8366, count)


if __name__ == "__main__":
    unittest.main()
