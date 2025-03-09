from heapq import heappush, heappop


def solution(n, start, end, roads, traps):

    start_node = start - 1
    end_node = end - 1

    trap_nodes = sorted([t - 1 for t in traps])
    trap_to_bit = {node: i for i, node in enumerate(trap_nodes)}

    graph_forward = [[] for _ in range(n)]
    graph_reverse = [[] for _ in range(n)]

    for a, b, cost in roads:
        a -= 1
        b -= 1
        graph_forward[a].append((b, cost))
        graph_reverse[b].append((a, cost))

    num_states = 1 << len(trap_to_bit)
    distances = [[float("inf")] * num_states for _ in range(n)]

    distances[start_node][0] = 0
    heap = [(0, start_node, 0)]

    def is_original_direction(state, node, next_node):

        node_active = state & (1 << trap_to_bit[node]) if node in trap_to_bit else 0
        next_active = (
            state & (1 << trap_to_bit[next_node]) if next_node in trap_to_bit else 0
        )
        return (bool(node_active) and bool(next_active)) or (
            not bool(node_active) and not bool(next_active)
        )

    while heap:
        total_cost, cur_node, cur_state = heappop(heap)

        if total_cost > distances[cur_node][cur_state]:
            continue

        for next_node, edge_cost in graph_forward[cur_node]:
            if not is_original_direction(cur_state, cur_node, next_node):
                continue

            next_cost = total_cost + edge_cost
            next_state = cur_state

            if next_node in trap_to_bit:
                next_state ^= 1 << trap_to_bit[next_node]
            if next_cost < distances[next_node][next_state]:
                distances[next_node][next_state] = next_cost
                heappush(heap, (next_cost, next_node, next_state))

        for next_node, edge_cost in graph_reverse[cur_node]:
            if is_original_direction(cur_state, cur_node, next_node):
                continue

            next_cost = total_cost + edge_cost
            next_state = cur_state
            if next_node in trap_to_bit:
                next_state ^= 1 << trap_to_bit[next_node]
            if next_cost < distances[next_node][next_state]:
                distances[next_node][next_state] = next_cost
                heappush(heap, (next_cost, next_node, next_state))

    return min(distances[end_node])
