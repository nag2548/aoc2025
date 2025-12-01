TOTAL_NUMBERS = 100


def read_file() -> list[str]:
    with open("../inputs/day1.txt") as f:
        return [l.rstrip("\n") for l in f]


def left(curr: int, number: int) -> int:
    return (curr - number) % TOTAL_NUMBERS


def right(curr: int, number: int) -> int:
    return (curr + number) % TOTAL_NUMBERS


if __name__ == "__main__":
    lines = read_file()
    start = 50
    zeroCounter = 0
    moves = {"L": left, "R": right}

    for line in lines:
        direction = line[0]
        start = moves[direction](start, int(line[1:]))

        print(f"new start: {start}")
        if start == 0:
            zeroCounter += 1

    print(f"hit zero {zeroCounter} times")
