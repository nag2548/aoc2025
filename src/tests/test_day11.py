import unittest

from src.days import day11


class TestDay11(unittest.TestCase):
    def test_part1(self):
        result = day11.part1()
        self.assertEqual(640, result)

    def test_part2(self):
        result = day11.part2()
        self.assertEqual(367579641755680, result)


if __name__ == "__main__":
    unittest.main()
