import unittest

from src.day1 import run as part1
from src.day1_part2 import run as part2


class Day1Tests(unittest.TestCase):
    def test_part1(self):
        result = part1()
        self.assertEqual(result, 992, "The result is wrong")

    def test_part2(self):
        result = part2()
        self.assertEqual(result, 6133, "The result is wrong")


if __name__ == "__main__":
    unittest.main()
