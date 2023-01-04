from typing import Tuple, List
import sys


class BF:
    INF = int(1e9)

    def __init__(self, v: List[int], e: List[Tuple[int, int, int]]):
        assert (v != None and len(v) > 1)
        self.v, self.e = v, e
        self.lastVertex = v[-1]
        self.distance = [self.INF] * (len(v)+1)

    def bellman_ford(self, start):
        self.distance[start] = 0

        # Iterate for all vertexes
        for v in self.v:
            # Iterate for all edges
            for e in self.e:
                cur, next, cost = e[0], e[1], e[2]
                # If already visited and Cost of traverse start to next (the smallest untill now on, start -> next)
                # is larger than that of via current node (start -> current -> next).
                if self.distance[cur] != self.INF and self.distance[next] > self.distance[cur] + cost:
                    self.distance[next] = self.distance[cur] + cost
                    # Any value is updated on last vertex where means at least one negative edge exists.
                    if v == self.lastVertex:
                        return True
        return False


"""
Time: O(VE)
"""

# https://www.acmicpc.net/problem/11657

input = sys.stdin.readline
v, e = map(int, input().split())
vertex = [i+1 for i in range(v)]
edge = [tuple(map(int, input().split())) for _ in range(e)]

bf = BF(vertex, edge)
cycle = bf.bellman_ford(1)

if cycle:
    print("-1")
else:
    for i in range(2, v+1):
        if bf.distance[i] == bf.INF:
            print("-1")
        else:
            print(bf.distance[i])
