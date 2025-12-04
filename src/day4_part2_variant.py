import sys
from pathlib import Path

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


def read_file() -> list[str]:
    input_path = Path(__file__).parent.parent / "inputs" / "day4.txt"
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def get_adjacent_rolls(tile, rolls):
    count = 0
    for pos in NEIGHBORS:
        x, y = tile
        offset_x, offset_y = pos
        neighbor = (x + offset_x, y + offset_y)
        if neighbor in rolls:
            count += 1
    return count


def count_rolls():
    lines = read_file()
    count, max_y, max_x = 0, len(lines), len(lines[0])
    rolls = {
        (x, y)
        for y, line in enumerate(lines)
        for x, tile in enumerate(line)
        if tile == ROLL
    }

    while True:
        min_rolls = sys.maxsize
        for row in range(max_y):
            for col in range(max_x):
                tile = (col, row)
                if tile in rolls:
                    adjacent_rolls = get_adjacent_rolls(tile, rolls)
                    min_rolls = min(min_rolls, adjacent_rolls)
                    if adjacent_rolls < 4:
                        count += 1
                        rolls.remove(tile)
        if min_rolls >= 4:
            break

    print(f"roll count: {count}")
    return count


if __name__ == "__main__":
    count_rolls()
