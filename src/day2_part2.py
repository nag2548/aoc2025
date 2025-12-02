import itertools
from pathlib import Path


def get_input() -> str:
    input_path = Path(__file__).parent.parent / "inputs" / "day2.txt"
    with open(input_path, "r") as f:
        return f.read()


def get_invalid_ids_sum():
    line = get_input()
    id_list = [pair.split("-") for pair in line.split(",")]
    id_sum = 0

    for pair in id_list:
        for i in range(int(pair[0]), int(pair[1]) + 1):
            string_value = str(i)
            for chunk in range(1, (len(string_value) // 2) + 1):
                if len(string_value) % chunk != 0:
                    continue
                chunks = list(itertools.batched(string_value, chunk))
                if len({*chunks}) == 1:
                    id_sum += i
                    break

    print(f"invalid ids sum: {id_sum}")
    return id_sum


if __name__ == "__main__":
    get_invalid_ids_sum()
