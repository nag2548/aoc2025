import operator

from src.helpers.file_helper import read_file_as_list


def solve_worksheet():
    lines = read_file_as_list("day6.txt")
    rows = len(lines)
    cols = len(lines[0].split())
    problems = [["0"] * rows for _ in range(cols)]

    for row in range(rows):
        splits = list(lines[row].split())
        for col in range(cols):
            problems[col][row] = splits[col]

    total = 0
    for problem in problems:
        last = problem[-1]
        operation = operator.add if last == "+" else operator.mul

        result = int(problem[0])
        for a in problem[1:-1]:
            result = operation(result, int(a))
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
