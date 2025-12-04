from src.file_helper import read_file_as_list


def get_total_joltage():
    total = 0
    lines = read_file_as_list("day3.txt")

    for line in lines:
        first = int(line[0])
        second = int(line[1])
        for c in line[2:]:
            curr = int(c)
            now = first * 10 + second
            a = first * 10 + curr
            b = second * 10 + curr
            if a > now and a > b:
                second = curr
            elif b > now:
                first = second
                second = curr

        total += first * 10 + second

    print(f"joltage sum: {total}")
    return total


if __name__ == "__main__":
    get_total_joltage()
