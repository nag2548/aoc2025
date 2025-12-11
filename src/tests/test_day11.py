import unittest

from src.days import day11


class TestDay11(unittest.TestCase):
    def test_part1(self):
        result = day11.solve()
        self.assertEqual(640, result)


if __name__ == "__main__":
    unittest.main()
