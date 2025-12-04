from src.file_helper import read_file_as_string


def get_invalid_ids_sum():
    line = read_file_as_string("day2.txt")
    id_list = (pair.split("-") for pair in line.split(","))
    id_sum = 0

    for start, end in id_list:
        for i in range(int(start), int(end) + 1):
            string_value = str(i)
            for chunk in range(1, (len(string_value) // 2) + 1):
                if len(string_value) % chunk != 0:
                    continue
                if string_value == string_value[:chunk] * (len(string_value) // chunk):
                    id_sum += i
                    break

    print(f"invalid ids sum: {id_sum}")
    return id_sum


if __name__ == "__main__":
    get_invalid_ids_sum()
