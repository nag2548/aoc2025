import unittest

from src.days import day9


class TestDay9(unittest.TestCase):
    def test_part1(self):
        result = day9.solve()
        self.assertEqual(50, result)


if __name__ == "__main__":
    unittest.main()
