import sys

input = sys.stdin.readline
answer = 0
g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
planes = [int(input()) for _ in range(p)]


def find(x):
    if parent[x] != x:
        parent[x] = parent[find(parent[x])]
    return parent[x]


for plane in planes:
    docking = find(plane)
    if docking == 0:
        break
    parent[docking] = parent[docking - 1]
    answer += 1

print(answer)
