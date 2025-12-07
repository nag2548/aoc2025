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
                left = (next_x - 1, next_y)
                if left in manifold:
                    queue.append(left)
                right = (next_x + 1, next_y)
                if right in manifold:
                    queue.append(right)

    print(f"Split count: {split_count}")
    return split_count


def factorial(pos, manifold, factorial_memo):
    x, y = pos
    if pos not in manifold:
        return 1
    if pos not in factorial_memo:
        if manifold[pos][2] == SPLITTER:
            factorial_memo[pos] = factorial(
                (x - 1, y), manifold, factorial_memo
            ) + factorial((x + 1, y), manifold, factorial_memo)
        else:
            factorial_memo[pos] = factorial((x, y + 1), manifold, factorial_memo)
    return factorial_memo[pos]


def count_splits_2():
    lines = read_file_as_list("day7.txt")
    manifold, start = init_manifold(lines)
    factorial_memo = {}
    timeline_count = factorial(start, manifold, factorial_memo)
    print(f"timeline count: {timeline_count}")
    return timeline_count


if __name__ == "__main__":
    count_splits()
    count_splits_2()
