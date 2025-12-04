from src.file_helper import read_file_as_string


def get_invalid_ids_sum():
    line = read_file_as_string("day2.txt")
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
