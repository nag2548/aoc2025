from pathlib import Path

TOTAL_NUMBERS = 100


def read_file() -> list[str]:
    input_path = Path(__file__).parent.parent / "inputs" / "day1.txt"
    with open(input_path, "r") as f:
        return f.read().splitlines()


def shift(curr: int, number: int, right_turn: bool) -> int:
    factor = 1 if right_turn else -1
    return (curr + number * factor) % TOTAL_NUMBERS


def run() -> int:
    lines = read_file()
    start = 50
    zero_counter = 0

    for line in lines:
        direction = line[0]
        start = shift(start, int(line[1:]), direction == "R")

        if start == 0:
            zero_counter += 1

    print(f"hit zero {zero_counter} times")
    return zero_counter


if __name__ == "__main__":
    run()
