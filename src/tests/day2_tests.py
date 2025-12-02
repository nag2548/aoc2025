import unittest

from src import day2


class Day2Tests(unittest.TestCase):
    def test_part_1(self):
        sum = day2.get_invalid_ids_sum()
        self.assertEqual(12850231731, sum)
