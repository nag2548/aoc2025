import operator

from src.helpers.file_helper import read_file_as_list

OPERATOR_MAP = {
    "+": operator.add,
    "*": operator.mul,
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
        result = 0 if operators[i] == "+" else 1
        for a in problem:
            result = op(result, a)
        total += result

    print(f"total: {total}")
    return total


def solve_worksheet_2():
    lines = read_file_as_list("day6.txt")
    problems = {}
    operators = list(
        map(
            lambda o: operator.add if o == "+" else operator.mul,
            reversed(lines[-1].split()),
        )
    )

    for line in lines[:-1]:
        for col, x in enumerate(line):
            problems[col] = problems.get(col, "") + x

    total = 0
    i = 0
    line_result = 0 if operators[i] == operator.add else 1
    for _, value in sorted(problems.items(), reverse=True):
        stripped = value.strip()
        if not stripped:
            i += 1
            total += line_result
            line_result = 0 if operators[i] == operator.add else 1
            continue
        line_result = operators[i](line_result, int(value))
    total += line_result

    print(f"total: {total}")
    return total


if __name__ == "__main__":
    solve_worksheet()
    solve_worksheet_2()
