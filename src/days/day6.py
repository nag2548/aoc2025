import numpy as np

from src.helpers.file_helper import read_file_as_list

OPERATOR_MAP = {
    "+": np.sum,
    "*": np.prod,
}


def solve_worksheet():
    lines = read_file_as_list("day6.txt")
    operators = lines[-1].split()
    problems = [[] for _ in range(len(lines[0].split()))]
    for row in lines[:-1]:
        splits = row.split()
        for col, split in enumerate(splits):
            problems[col].append(int(split))

    total = 0
    for i, problem in enumerate(problems):
        op = OPERATOR_MAP[operators[i]]
        total += op(problem)

    print(f"total: {total}")
    return total


def solve_worksheet_2():
    lines = read_file_as_list("day6.txt")
    problems = ["" for _ in range(len(lines[0]))]
    operators = list(reversed(lines[-1].split()))

    for line in lines[:-1]:
        for col, x in enumerate(line):
            problems[col] = problems[col] + x

    total = i = 0
    col_numbers = []
    for value in reversed(problems):
        stripped = value.strip()
        if not stripped:
            total += OPERATOR_MAP[operators[i]](col_numbers)
            col_numbers = []
            i += 1
            continue
        col_numbers.append(int(value))
    total += OPERATOR_MAP[operators[-1]](col_numbers)

    print(f"total: {total}")
    return total


if __name__ == "__main__":
    solve_worksheet()
    solve_worksheet_2()
