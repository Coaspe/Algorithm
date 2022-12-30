import heapq
import sys
from collections import defaultdict
from typing import List, Tuple

INF = sys.maxsize


class DJ:
    def genGraph(self):
        self.graph = defaultdict(list)
        for s, e, c in self.edges:
            self.graph[s].append((e, c))

    def __init__(self, start, edges: List[Tuple[int, int, int]], n) -> None:
        self.dist = [INF] * n
        self.edges = edges
        self.genGraph()
        self.dist[start] = 0
        queue = []
        heapq.heappush(queue, (self.dist[start], start))

    def dijkstra(self):
        while self.queue:
            cur_dist, cur_dest = heapq.heappop(self.queue)

            if self.dist[cur_dest] < cur_dist:
                continue

            for new_dest, new_dist in self.graph[cur_dest]:
                dist = cur_dist + new_dist
                if dist < self.dist[new_dest]:
                    self.dist[new_dest] = dist
                    heapq.heappush(self.queue, (dist, new_dest))

        return self.dist


"""
Time: O(ElogV)
"""
