from src.helpers.file_helper import read_file_as_list

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


def get_adjacent_rolls(roll, rolls):
    return sum(
        (roll[0] + offset_x, roll[1] + offset_y) in rolls
        for offset_x, offset_y in NEIGHBORS
    )


def build_grid_set(lines: list[str]) -> set[tuple[int, int]]:
    return {
        (x, y)
        for y, line in enumerate(lines)
        for x, tile in enumerate(line)
        if tile == ROLL
    }


def count_rolls():
    lines = read_file_as_list("day4.txt")
    rolls = build_grid_set(lines)

    count = sum(get_adjacent_rolls(roll, rolls) < 4 for roll in rolls)

    print(f"roll count: {count}")
    return count


def count_rolls_2():
    lines = read_file_as_list("day4.txt")
    count = 0
    rolls = build_grid_set(lines)

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
