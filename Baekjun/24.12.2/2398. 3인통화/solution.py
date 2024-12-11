import heapq
from typing import List, Tuple, Set


def dijkstra(
    graph: List[List[Tuple[int, int]]], start: int, n: int
) -> Tuple[List[int], List[Tuple[int, int]]]:
    inf = float("inf")
    distances = [inf] * (n + 1)
    distances[start] = 0

    pq = [(0, start)]

    prev = [(-1, 0)] * (n + 1)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for next_node, edge_cost in graph[current_node]:
            distance = current_dist + edge_cost

            if distance < distances[next_node]:
                distances[next_node] = distance
                prev[next_node] = (current_node, edge_cost)
                heapq.heappush(pq, (distance, next_node))

    return distances, prev


def track_path(prev: List[Tuple[int, int]], node: int) -> Set[Tuple[int, int, int]]:
    path_edges = set()
    current = node

    while prev[current][0] != -1:
        prev_node, edge_cost = prev[current]
        path_edges.add(tuple(sorted([prev_node, current]) + [edge_cost]))
        current = prev_node

    return path_edges


def solve_multi_target_shortest_path(
    n: int, graph: List[List[Tuple[int, int]]], targets: List[int]
) -> None:
    dijkstra_results = [dijkstra(graph, target, n) for target in targets]

    optimal_node = min(
        range(1, n + 1),
        key=lambda x: sum(distances[x] for distances, _ in dijkstra_results),
    )

    all_path_edges = set()
    for _, prev in dijkstra_results:
        all_path_edges.update(track_path(prev, optimal_node))

    sorted_edges = sorted(all_path_edges)

    total_cost = sum(cost for _, _, cost in sorted_edges)

    print(total_cost, len(sorted_edges))
    for a, b, _ in sorted_edges:
        print(f"{a} {b}")


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    targets = list(map(int, input().split()))

    solve_multi_target_shortest_path(n, graph, targets)


if __name__ == "__main__":
    main()
