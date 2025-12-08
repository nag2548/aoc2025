from operator import itemgetter

import numpy as np

from src.helpers.file_helper import read_file_as_list


def find(x, graph):
    if graph[x] != x:
        graph[x] = find(graph[x], graph)
    return graph[x]


def union(a, b, graph):
    root_a = find(a, graph)
    root_b = find(b, graph)
    if root_a != root_b:
        graph[root_b] = root_a


def solve_1(connections):
    lines = read_file_as_list("day8.txt")
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

    edges = sorted(distances, key=itemgetter(2))[slice(connections)]

    graph = {}
    for a, b, _ in edges:
        graph.setdefault(a, a)
        graph.setdefault(b, b)

    for a, b, _ in edges:
        union(a, b, graph)

    components = {}
    for node in graph:
        root = find(node, graph)
        components.setdefault(root, []).append(node)

    lengths = [
        len(group) for group in sorted(components.values(), key=len, reverse=True)
    ]
    result = np.prod(lengths[:3])
    print(f"result: {result}")
    return result


if __name__ == "__main__":
    solve_1(10)
