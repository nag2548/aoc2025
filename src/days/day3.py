import sys

from src.helpers.file_helper import read_file_as_list


def get_total_joltage():
    total = 0
    lines = read_file_as_list("day3.txt")

    for line in lines:
        first = int(line[0])
        second = int(line[1])
        for c in line[2:]:
            curr = int(c)
            now = first * 10 + second
            a = first * 10 + curr
            b = second * 10 + curr
            if a > now and a > b:
                second = curr
            elif b > now:
                first = second
                second = curr

        total += first * 10 + second

    print(f"joltage sum: {total}")
    return total


def get_total_joltage_2() -> int:
    total = 0
    window = 12

    for line in read_file_as_list("day3.txt"):
        line_result = ""
        n = len(line)
        i = 0
        while len(line_result) < window:
            current_max = -sys.maxsize
            current_window = window - len(line_result)

            last_idx = i
            for j in range(n - current_window - i + 1):
                curr_val = int(line[i + j])
                if curr_val > current_max:
                    current_max = curr_val
                    last_idx = i + j
            line_result += str(current_max)
            i = last_idx + 1
        total += int(line_result)

    print(f"total: {total}")
    return total


if __name__ == "__main__":
    get_total_joltage()
    get_total_joltage_2()
