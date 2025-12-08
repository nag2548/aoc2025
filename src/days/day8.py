from operator import itemgetter

import numpy as np

from src.helpers.file_helper import read_file_as_list


def solve_1():
    lines = read_file_as_list("day8_example.txt")
    vectors = [tuple(map(int, line.split(","))) for line in lines]

    distances = []
    for i, a in enumerate(vectors):
        x1, y1, z1 = a
        for b in vectors[i + 1 :]:
            x2, y2, z2 = b
            distances.append(
                (
                    a,
                    b,
                    np.sqrt(
                        np.pow(x1 - x2, 2) + np.pow(y1 - y2, 2) + np.pow(z1 - z2, 2)
                    ),
                )
            )
    for d in sorted(distances, key=itemgetter(2)):
        print(d)

    return 0


if __name__ == "__main__":
    solve_1()
