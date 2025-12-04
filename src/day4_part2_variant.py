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


def get_adjacent_rolls(roll, rolls):
    return sum(
        (roll[0] + offset_x, roll[1] + offset_y) in rolls
        for offset_x, offset_y in NEIGHBORS
    )


def count_rolls():
    lines = read_file()
    count = 0
    rolls = {
        (x, y)
        for y, line in enumerate(lines)
        for x, tile in enumerate(line)
        if tile == ROLL
    }

    while True:
        rolls_to_remove = set()
        for roll in rolls:
            adjacent_rolls = get_adjacent_rolls(roll, rolls)
            if adjacent_rolls < 4:
                count += 1
                rolls_to_remove.add(roll)
        if len(rolls_to_remove) == 0:
            break
        rolls = rolls - rolls_to_remove

    print(f"roll count: {count}")
    return count


if __name__ == "__main__":
    count_rolls()
