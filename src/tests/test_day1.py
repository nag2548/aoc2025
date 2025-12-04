import unittest

from src.days import day1


class Day1Tests(unittest.TestCase):
    def test_part1(self):
        result = day1.part1()
        self.assertEqual(992, result, "The result is wrong")

    def test_part2(self):
        result = day1.part2()
        self.assertEqual(6133, result, "The result is wrong")


if __name__ == "__main__":
    unittest.main()
