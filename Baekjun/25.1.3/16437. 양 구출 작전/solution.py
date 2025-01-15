from sys import setrecursionlimit, stdin

input = stdin.readline

setrecursionlimit(10**5)
N = int(input())

G = [[] for _ in range(N + 1)]
A = [(0, 0, 0), (0, 0, 0)]

for i in range(2, N + 1):
    inp = input().split()
    sw, a, p = inp[0], int(inp[1]), int(inp[2])
    G[p].append(i)
    if sw == "W":
        a *= -1
    A.append((sw, a, p))


def dfs(node):
    ww = A[node][1]

    for next_node in G[node]:
        val = dfs(next_node)
        if val > 0:
            ww += val

    return ww


print(dfs(1))
