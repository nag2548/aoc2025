from pathlib import Path

TOTAL_NUMBERS = 100


def read_file() -> list[str]:
    input_path = Path(__file__).parent.parent / "inputs" / "day1.txt"
    with open(input_path, "r") as f:
        return f.read().splitlines()


def shift(curr: int, number: int, right_turn: bool) -> dict[str, int]:
    factor = 1 if right_turn else -1
    shifted = curr + number * factor

    hits = abs(shifted // TOTAL_NUMBERS)

    if curr == 0 and not right_turn:
        hits -= 1
    if shifted % TOTAL_NUMBERS == 0 and not right_turn:
        hits += 1

    return {"next": shifted % TOTAL_NUMBERS, "hits": hits}


def run() -> int:
    lines = read_file()
    start = 50
    zero_counter = 0

    for line in lines:
        number = int(line[1:])
        direction = line[0] == "R"
        results = shift(start, number, direction)
        zero_counter += results["hits"]
        start = results["next"]

    print(f"hit zero {zero_counter} times")
    return zero_counter


if __name__ == "__main__":
    run()
