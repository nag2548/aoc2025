TOTAL_NUMBERS = 100


def read_file() -> list[str]:
    with open("../inputs/day1.txt") as f:
        return [l.rstrip("\n") for l in f]


def left(curr: int) -> int:
    return (curr - 1) % TOTAL_NUMBERS


def right(curr: int) -> int:
    return (curr + 1) % TOTAL_NUMBERS


if __name__ == "__main__":
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
        print(f"new start: {start}")
    print(f"hit zero {zero_counter} times")
