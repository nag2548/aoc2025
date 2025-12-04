import unittest

from src.days import day2


class Day2Tests(unittest.TestCase):
    def test_part_1(self):
        id_sum = day2.get_invalid_ids_sum()
        self.assertEqual(12850231731, id_sum)

    def test_part_2(self):
        id_sum = day2.get_invalid_ids_sum_2()
        self.assertEqual(24774350322, id_sum)


if __name__ == "__main__":
    unittest.main()
