import unittest

from src.days import day10


class TestDay10Case(unittest.TestCase):
    def test_part1(self):
        result = day10.solve()
        self.assertEqual(422, result)


if __name__ == "__main__":
    unittest.main()
