from src.helpers.file_helper import read_file_as_list


EMPTY_SPACE = "."
SPLITTER = "^"
START = "S"


def init_manifold(lines: list[str]):
    manifold, start = {}, None
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            manifold[(col, row)] = (col, row, char)
            if char == START:
                start = (col, row)
    return manifold, start


def count_splits():
    lines = read_file_as_list("day7.txt")
    manifold, start = init_manifold(lines)
    split_count, unique_split_locations = 0, set()
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        if (x, y + 1) in manifold:
            next_x, next_y, next_char = manifold[(x, y + 1)]
            if next_char == EMPTY_SPACE:
                queue.append((next_x, next_y))
            elif next_char == SPLITTER:
                if (next_x, next_y) in unique_split_locations:
                    continue
                unique_split_locations.add((next_x, next_y))
                split_count += 1
                if (next_x - 1, next_y) in manifold:
                    queue.append((next_x - 1, next_y))
                if (next_x + 1, next_y) in manifold:
                    queue.append((next_x + 1, next_y))

    print(f"Split count: {split_count}")
    return split_count


def count_splits_2():
    lines = read_file_as_list("day7_example.txt")
    manifold, start = init_manifold(lines)
    return None


if __name__ == "__main__":
    count_splits()
