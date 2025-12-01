total_numbers = 100
zeroCounter = 0


def read_file() -> list[str]:
    with open("../inputs/day1.txt") as f:
        return [l.rstrip("\n") for l in f]


def left(curr: int) -> int:
    return (curr - 1) % total_numbers


def right(curr: int) -> int:
    return (curr + 1) % total_numbers


if __name__ == "__main__":
    lines = read_file()
    start = 50

    for line in lines:
        number = (
            int(line.lstrip("L")) if line.startswith("L") else int(line.lstrip("R"))
        )
        for _ in range(number):
            if line.startswith("L"):
                start = left(start)
            else:
                start = right(start)
            if start == 0:
                zeroCounter += 1
        print(f"new start: {start}")
    print(f"hit zero {zeroCounter} times")
