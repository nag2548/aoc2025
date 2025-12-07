import unittest

from src.days import day7


class TestDay7(unittest.TestCase):
    def test_part_1(self):
        count = day7.count_splits()
        self.assertEqual(1592, count)


if __name__ == "__main__":
    unittest.main()
