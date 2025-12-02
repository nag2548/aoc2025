import unittest

import src.day2 as part1
import src.day2_part2 as part2


class Day2Tests(unittest.TestCase):
    def test_part_1(self):
        id_sum = part1.get_invalid_ids_sum()
        self.assertEqual(12850231731, id_sum)

    def test_part_2(self):
        id_sum = part2.get_invalid_ids_sum()
        self.assertEqual(24774350322, id_sum)


if __name__ == "__main__":
    unittest.main()
