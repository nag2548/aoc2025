from src.helpers.file_helper import read_file_as_list


def find_paths(node, graph):
    if node == "out":
        return 1
    return sum(find_paths(ref, graph) for ref in graph[node])


def solve():
    lines = read_file_as_list("day11.txt")
    graph = {}
    for line in lines:
        split = line.split(": ")
        graph[split[0]] = split[1].split(" ")

    paths = find_paths("you", graph)
    print(f"paths: {paths}")
    return paths


if __name__ == "__main__":
    solve()
