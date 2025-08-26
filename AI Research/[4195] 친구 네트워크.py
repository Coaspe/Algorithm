from collections import defaultdict
from sys import stdin

input = stdin.readline


def find(x, dic):
    if dic[x] == x:
        return x

    dic[x] = find(dic[x], dic)

    return dic[x]


def union(x, y, dic, size):
    xx = find(x, dic)
    yy = find(y, dic)

    if xx == yy:
        return size[xx]

    if size[xx] > size[yy]:
        dic[xx] = yy
        size[yy] += size[xx]
    else:
        dic[yy] = xx
        size[xx] += size[yy]
        yy = xx
    return size[yy]


for _ in range(int(input())):
    N = int(input())
    P = defaultdict(str)
    S = defaultdict(int)
    for _ in range(N):
        a, b = input().split()

        if a not in P:
            P[a] = a
            S[a] = 1
        if b not in P:
            P[b] = b
            S[b] = 1

        print(union(a, b, P, S))
