from collections import defaultdict
from math import dist
from operator import itemgetter
from typing import Any

import numpy as np

from src.helpers.file_helper import read_file_as_list


def solve_1(connections):
    lines = read_file_as_list("day8.txt")
    vectors = [tuple(map(int, line.split(","))) for line in lines]

    distances, nodes = init_edges_and_nodes(vectors)
    edges = sorted(distances, key=itemgetter(2))[:connections]
    graph = defaultdict(list)
    for a, b, _ in edges:
        graph[a].append(b)
        graph[b].append(a)

    groups = []
    for node in graph:
        group = []
        if node in nodes:
            dfs(node, nodes, graph, group)
        groups.append(group)

    lengths = sorted([len(group) for group in groups], reverse=True)
    result = np.prod(lengths[:3])
    print(f"result: {result}")
    return result


def solve_2():
    lines = read_file_as_list("day8.txt")
    vectors = [tuple(map(int, line.split(","))) for line in lines]

    distances, nodes = init_edges_and_nodes(vectors)

    edges = sorted(distances, key=itemgetter(2))
    graph = defaultdict(list)
    node_copy = set(nodes)
    last_edge = None
    for a, b, _ in edges:
        graph[a].append(b)
        graph[b].append(a)
        last_edge = (a, b)

        for node in graph:
            if node in node_copy:
                dfs(node, node_copy, graph, [])

        if not node_copy:
            break
        node_copy = set(nodes)

    a, b = last_edge
    result = a[0] * b[0]
    print(f"result: {result}")
    return result


def init_edges_and_nodes(vectors: list[tuple[int, ...]]) -> tuple[list[Any], set[Any]]:
    distances = []
    nodes = set()
    for i, a in enumerate(vectors):
        nodes.add(a)
        for b in vectors[i + 1 :]:
            distances.append((a, b, dist(a, b)))
    return distances, nodes


def dfs(node, node_copy, graph, group):
    node_copy.remove(node)
    group.append(node)
    for child in graph[node]:
        if child in node_copy:
            dfs(child, node_copy, graph, group)


if __name__ == "__main__":
    solve_2()
