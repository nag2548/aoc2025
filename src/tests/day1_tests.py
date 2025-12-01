import unittest

import src.day1 as part1
import src.day1_part2 as part2


class Day1Tests(unittest.TestCase):
    def test_part1(self):
        result = part1.run()
        self.assertEqual(992, result, "The result is wrong")

    def test_part2(self):
        result = part2.run()
        self.assertEqual(6133, result, "The result is wrong")


if __name__ == "__main__":
    unittest.main()
