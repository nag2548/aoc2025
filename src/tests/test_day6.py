import unittest

from src.days import day6


class TestDay6(unittest.TestCase):
    def test_day6(self):
        result = day6.solve_worksheet()
        self.assertEqual(6605396225322, result)


if __name__ == "__main__":
    unittest.main()
