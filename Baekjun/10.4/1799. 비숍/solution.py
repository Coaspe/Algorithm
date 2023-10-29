from sys import stdin

input = stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

lst = [[] for _ in range(2 * N)]

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            lst[i + j].append((i, j))


def dfs(idx, cnt):
    global ans

    if ans >= (cnt + (L + 1 - idx) // 2):
        return

    if idx >= L:
        ans = max(ans, cnt)
        return

    for ci, cj in lst[idx]:
        if v[ci - cj] == 0:
            v[ci - cj] = 1
            dfs(idx + 2, cnt + 1)
            v[ci - cj] = 0

    dfs(idx + 2, cnt)


L = 2 * N - 1
v = [0] * (2 * N)

ans = 0
dfs(0, 0)
W = ans

ans = 0
dfs(1, 0)
B = ans

print(W + B)
