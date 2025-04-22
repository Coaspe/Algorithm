import sys

input = sys.stdin.readline

N = int(input())
G = [int(input(), 2) for _ in range(N)]

for _ in range(int(input())):
    u, v = map(int, input().split())
    print((G[u - 1] & G[v - 1]).bit_count())
