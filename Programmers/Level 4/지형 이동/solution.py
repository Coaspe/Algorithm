from collections import deque
from heapq import heappop, heappush


def solution(land, height):
    n = len(land)
    total_cost = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[False] * n for _ in range(n)]

    candidate_heap = []
    candidate_costs = [[float("inf")] * n for _ in range(n)]

    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                diff = abs(land[r][c] - land[nr][nc])

                if diff > height:
                    if candidate_costs[nr][nc] > diff:
                        candidate_costs[nr][nc] = diff
                        heappush(candidate_heap, (diff, nr, nc))
                else:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        if not queue:
            while candidate_heap:
                cost, r, c = heappop(candidate_heap)
                if visited[r][c]:
                    continue
                visited[r][c] = True
                total_cost += cost
                queue.append((r, c))
                break

    return total_cost
