from itertools import combinations
from operator import itemgetter

from shapely import box, Polygon

from src.helpers.file_helper import read_file_as_list


def solve():
    lines = read_file_as_list("day9.txt")
    tiles = [tuple(map(int, line.split(","))) for line in lines]
    pairs = [
        (a, b, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
        for i, a in enumerate(tiles)
        for b in tiles[i + 1 :]
    ]
    pairs.sort(key=itemgetter(2))

    result = pairs[-1][2]
    print(f"result day 9: {result}")
    return result


def solve_2():
    lines = read_file_as_list("day9.txt")
    tiles = [tuple(map(int, line.split(","))) for line in lines]
    pairs = [
        (a, b, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
        for a, b in combinations(tiles, 2)
    ]

    largest_area = None
    poly = Polygon(tiles)
    for (ax, ay), (bx, by), area in sorted(pairs, key=itemgetter(2), reverse=True):
        if poly.contains(box(min(ax, bx), min(ay, by), max(ax, bx), max(ay, by))):
            largest_area = area
            break

    print(f"result day 9, part 2: {largest_area}")
    return largest_area


if __name__ == "__main__":
    solve()
    solve_2()
