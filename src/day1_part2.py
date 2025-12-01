from pathlib import Path

TOTAL_NUMBERS = 100


def read_file() -> list[str]:
    input_path = Path(__file__).parent.parent / "inputs" / "day1.txt"
    with open(input_path, "r") as f:
        return f.read().splitlines()


def left(curr: int) -> int:
    return (curr - 1) % TOTAL_NUMBERS


def right(curr: int) -> int:
    return (curr + 1) % TOTAL_NUMBERS


def run() -> int:
    lines = read_file()
    start = 50
    zero_counter = 0
    moves = {"L": left, "R": right}

    for line in lines:
        number = int(line[1:])

        for _ in range(number):
            start = moves[line[0]](start)
            if start == 0:
                zero_counter += 1
    print(f"hit zero {zero_counter} times")
    return zero_counter


if __name__ == "__main__":
    run()
