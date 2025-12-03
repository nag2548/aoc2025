import sys
from pathlib import Path


def read_file() -> list[str]:
    input_path = Path(__file__).parent.parent / "inputs" / "day3.txt"
    with open(input_path, "r") as f:
        return f.read().splitlines()


def get_total_joltage() -> int:
    total = 0
    window = 12

    for line in read_file():
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
