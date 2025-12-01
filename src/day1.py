total_numbers = 100


def read_file() -> list[str]:
    with open("../inputs/day1.txt") as f:
        return [l.rstrip("\n") for l in f]


def left(curr: int, number: int) -> int:
    return (curr - number) % total_numbers


def right(curr: int, number: int) -> int:
    return (curr + number) % total_numbers


if __name__ == "__main__":
    lines = read_file()
    start = 50
    zeroCounter = 0
    for line in lines:
        if line.startswith("L"):
            start = left(start, int(line.lstrip("L")))
        else:
            start = right(start, int(line.lstrip("R")))
        print(f"new start: {start}")
        if start == 0:
            zeroCounter += 1

    print(f"hit zero {zeroCounter} times")
