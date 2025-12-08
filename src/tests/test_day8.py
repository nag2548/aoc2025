import unittest

from src.days import day8


class TestDay8(unittest.TestCase):
    def test_part_1(self):
        result = day8.solve_1(1000)
        self.assertEqual(96672, result)

    def test_part_2(self):
        result = day8.solve_2()
        self.assertEqual(22517595, result)


if __name__ == "__main__":
    unittest.main()
