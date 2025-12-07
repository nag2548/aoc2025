from collections import deque

from src.helpers.file_helper import read_file_as_list

SPLITTER = "^"
START = "S"


def init_manifold(lines: list[str]):
    manifold, start = {}, None
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            manifold[(col, row)] = char
            if char == START:
                start = (col, row)
    return manifold, start


def count_splits():
    lines = read_file_as_list("day7.txt")
    manifold, start = init_manifold(lines)
    split_count, visited_splits = 0, set()
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        below = (x, y + 1)
        if below not in manifold:
            continue
        next_char = manifold[below]
        if next_char == SPLITTER:
            if below in visited_splits:
                continue
            visited_splits.add(below)
            split_count += 1
            for dx in (-1, 1):
                side = (x + dx, y + 1)
                if side in manifold:
                    queue.append(side)
        else:
            queue.append(below)

    print(f"Split count: {split_count}")
    return split_count


def factorial(pos, manifold, factorial_memo):
    x, y = pos
    if pos not in manifold:
        return 1
    if pos not in factorial_memo:
        if manifold[pos] == SPLITTER:
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
    print(f"Timeline count: {timeline_count}")
    return timeline_count


if __name__ == "__main__":
    count_splits()
    count_splits_2()
