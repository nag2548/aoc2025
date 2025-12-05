from operator import itemgetter

from src.helpers.file_helper import read_file_as_string


def count_fresh_ingredients():
    file = read_file_as_string("day5.txt").split("\n\n")
    ingredient_ids, available_ingredients = [
        tuple(map(int, line.split("-"))) for line in file[0].split("\n")
    ], list(map(int, file[1].strip().split("\n")))

    count = sum(
        any(id_entry[0] <= ingredient <= id_entry[1] for id_entry in ingredient_ids)
        for ingredient in available_ingredients
    )
    print(f"fresh ingredients: {count}")
    return count


def count_fresh_ingredients_2():
    file = read_file_as_string("day5.txt").split("\n\n")
    ingredient_ids = sorted(
        [tuple(map(int, line.split("-"))) for line in file[0].split("\n")],
        key=itemgetter(0),
    )

    n = len(ingredient_ids)
    merged_id_ranges = []
    for i in range(n):
        start, end = ingredient_ids[i]
        if merged_id_ranges and merged_id_ranges[-1][1] >= end:
            continue

        for j in range(i + 1, n):
            start_other, end_other = ingredient_ids[j]
            if start_other <= end:
                end = max(end, end_other)
        merged_id_ranges.append((start, end))

    count = sum(r[1] - r[0] + 1 for r in merged_id_ranges)
    print(f"fresh ingredients: {count}")
    return count


if __name__ == "__main__":
    count_fresh_ingredients()
