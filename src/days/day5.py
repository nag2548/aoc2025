from src.helpers.file_helper import read_file_as_string


def count_fresh_ingredients():
    count = 0
    file = read_file_as_string("day5.txt").split("\n\n")
    ingredient_ids, available_ingredients = [
        (list(map(int, line.split("-")))) for line in file[0].split("\n")
    ], list(map(int, file[1].strip().split("\n")))

    for ingredient in available_ingredients:
        if any(id_entry[0] <= ingredient <= id_entry[1] for id_entry in ingredient_ids):
            count += 1
    return count


if __name__ == "__main__":
    count_fresh_ingredients()
