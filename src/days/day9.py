from operator import itemgetter

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


if __name__ == "__main__":
    solve()
