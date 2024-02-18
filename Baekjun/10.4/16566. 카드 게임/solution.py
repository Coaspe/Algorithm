from bisect import bisect_left
from sys import stdin

input = stdin.readline

N, M, K = map(int, input().split())
MM = list(map(int, input().split()))
MM.sort()

S = list(map(int, input().split()))
parent = [i for i in range(M)]


def find(p):
    if p != parent[p]:
        parent[p] = find(parent[p])
    return parent[p]


def union(p1, p2):
    pp1 = find(p1)
    pp2 = find(p2)

    if pp1 > pp2:
        parent[p2] = pp1
    else:
        parent[p1] = pp2


for s in S:
    idx = bisect_left(MM, s)

    i = find(idx)

    if MM[i] == s:
        i = find(idx + 1)

    print(MM[i])

    if i < M - 1:
        union(i, i + 1)
