from typing import List

from src.helpers.file_helper import read_file_as_list


def path_counter(graph, start):
    memo = {}

    def find_paths_2(node, visited):
        if node == "dac":
            visited |= 1 << 0
        if node == "fft":
            visited |= 1 << 1

        if node == "out":
            return int(visited == 0b11)

        if (node, visited) in memo:
            return memo[(node, visited)]

        res = sum(find_paths_2(ref, visited) for ref in graph[node])
        memo[(node, visited)] = res
        return res

    return find_paths_2(start, 0)


def find_paths(node, graph):
    if node == "out":
        return 1
    return sum(find_paths(ref, graph) for ref in graph[node])


def init_graph(lines: list[str]) -> dict[str, List[str]]:
    return {k: v.split() for k, v in (line.split(": ") for line in lines)}


def part1():
    lines = read_file_as_list("day11.txt")
    graph = init_graph(lines)

    paths = find_paths("you", graph)
    print(f"paths: {paths}")
    return paths


def part2():
    lines = read_file_as_list("day11.txt")
    graph = init_graph(lines)
    paths = path_counter(graph, "svr")
    print(f"paths: {paths}")
    return paths


if __name__ == "__main__":
    part1()
    part2()
