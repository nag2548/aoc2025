import sys

from src.file_helper import read_file_as_string, read_file_as_list

NEIGHBORS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]
ROLL = "@"


def get_adjacent_rolls(tile, tiles):
    count = 0
    for pos in NEIGHBORS:
        x, y, _ = tile
        offset_x, offset_y = pos
        if (
            0 <= x + offset_x < len(tiles[0])
            and 0 <= y + offset_y < len(tiles)
            and tiles[y + offset_y][x + offset_x][2] == ROLL
        ):
            count += 1
    return count


def count_rolls():
    count = 0
    tiles = [
        [(x, y, tile) for x, tile in enumerate(line)]
        for y, line in enumerate(read_file_as_list("day4.txt"))
    ]

    while True:
        min_rolls = sys.maxsize
        for row in tiles:
            for tile in row:
                x, y, val = tile
                if val == ROLL:
                    adjacent_rolls = get_adjacent_rolls(tile, tiles)
                    min_rolls = min(min_rolls, adjacent_rolls)
                    if adjacent_rolls < 4:
                        count += 1
                        tiles[y][x] = (x, y, ".")
        if min_rolls >= 4:
            break

    print(f"roll count: {count}")
    return count


if __name__ == "__main__":
    count_rolls()
