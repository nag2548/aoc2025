import unittest

from src import day4 as part1


class Day4Tests(unittest.TestCase):
    def test_part1(self):
        count = part1.count_rolls()
        self.assertEqual(1409, count)


if __name__ == "__main__":
    unittest.main()
