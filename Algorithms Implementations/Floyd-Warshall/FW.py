import sys
from typing import Tuple, List
INF = sys.maxsize


class FW:

    def __init__(self, a: List[Tuple[int, int, int]], n: int) -> None:
        self.dist = [[INF]*n for _ in range(n)]
        self.n = n

        for s, e, c in a:
            self.dist[s-1][e-1] = min(self.dist[s-1][e-1], c)

    def floyd_warshall(self):
        # Via
        for k in range(self.n):
            # Start
            for i in range(self.n):
                # End
                for j in range(self.n):
                    if i != j:
                        self.dist[i][j] = min(
                            self.dist[i][j], self.dist[i][k] + self.dist[k][j])
        return self.dist


"""
Time: O(v^3)
"""
# https://www.acmicpc.net/problem/11404


input = sys.stdin.readline
N, B = int(input()), int(input())

a = [tuple(map(int, input().split())) for _ in range(B)]
fw = FW(a, N).floyd_warshall()

for i in range(N):
    for j in range(N):
        print(fw[i][j] if fw[i][j] != INF else 0, end=' ')
    print()
