from typing import List


class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))

    def find(self, x) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def join(self, parent, child) -> bool:
        child = self.find(child)
        parent = self.find(parent)

        if child == parent:
            return False

        self.parent[child] = parent

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all_edges = []
        n = len(points)

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                cur, nex = points[i], points[j]
                weight = abs(cur[0]-nex[0]) + abs(cur[1]-nex[1])
                all_edges.append((weight, i, j))

        all_edges.sort()
        uf = UnionFind(n)
        edge_used = 0
        answer = 0

        for weight, cur, nex in all_edges:
            if uf.join(cur, nex):
                edge_used += 1
                answer += weight
                if edge_used == n - 1:
                    break
        return answer
