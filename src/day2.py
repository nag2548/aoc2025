from pathlib import Path


def get_input() -> str:
    input_path = Path(__file__).parent.parent / "inputs" / "day2.txt"
    with open(input_path, "r") as f:
        return f.read()


def get_invalid_ids_sum():
    line = get_input()
    id_list = (pair.split("-") for pair in line.split(","))
    id_sum = 0

    for start, end in id_list:
        for i in range(int(start), int(end) + 1):
            string_value = str(i)
            if len(string_value) % 2 == 0:
                first = string_value[: (len(string_value) // 2)]
                second = string_value[(len(string_value) // 2) :]
                if first == second:
                    id_sum += i

    print(f"invalid ids sum: {id_sum}")
    return id_sum


if __name__ == "__main__":
    get_invalid_ids_sum()
