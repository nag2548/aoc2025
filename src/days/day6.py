import operator

from src.helpers.file_helper import read_file_as_list


def solve_worksheet():
    lines = read_file_as_list("day6.txt")
    rows = len(lines)
    cols = len(lines[0].split())
    problems = [["0"] * rows for _ in range(cols)]

    for row in range(rows):
        splits = [x for x in lines[row].split()]
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


if __name__ == "__main__":
    solve_worksheet()
