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
    split_count = 0
    beams = {start}
    while beams:
        next_beams = set()
        for beam in beams:
            x, y = beam
            if beam not in manifold:
                break

            if manifold[beam] == SPLITTER:
                split_count += 1
                next_beams.add((x - 1, y + 1))
                next_beams.add((x + 1, y + 1))
            else:
                next_beams.add((x, y + 1))
        beams = next_beams

    print(f"Split count: {split_count}")
    return split_count


def paths(pos, manifold, path_memo):
    x, y = pos
    if pos not in manifold:
        return 1
    if pos not in path_memo:
        if manifold[pos] == SPLITTER:
            path_memo[pos] = paths((x - 1, y), manifold, path_memo) + paths(
                (x + 1, y), manifold, path_memo
            )
        else:
            path_memo[pos] = paths((x, y + 1), manifold, path_memo)
    return path_memo[pos]


def count_splits_2():
    lines = read_file_as_list("day7.txt")
    manifold, start = init_manifold(lines)
    path_memo = {}
    timeline_count = paths(start, manifold, path_memo)
    print(f"Timeline count: {timeline_count}")
    return timeline_count


if __name__ == "__main__":
    count_splits()
    count_splits_2()
