import unittest

from src.days import day9


class TestDay9(unittest.TestCase):
    def test_part1(self):
        result = day9.solve()
        self.assertEqual(4776100539, result)

    def test_part2(self):
        result = day9.solve_2()
        self.assertEqual(1476550548, result)


if __name__ == "__main__":
    unittest.main()
