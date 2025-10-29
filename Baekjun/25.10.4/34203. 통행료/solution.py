from collections import deque

INF = 10**18


def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]


def union(par, h, x, y):
    x = find(par, x)
    y = find(par, y)
    if x == y:
        return
    if h[y] < h[x]:
        x, y = y, x
    h[y] += h[x]
    par[x] = y


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = [None] * (m + 1)
    v = [[] for _ in range(n + 1)]

    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0

    for i in range(1, m + 1):
        x, y = map(int, input().split())
        p[i] = (x, y)
        v[x].append(y)
        v[y].append(x)

    # BFS로 모든 쌍 최단거리 계산
    for i in range(1, n + 1):
        dp[i][i] = 0
        q = deque([i])
        while q:
            x = q.popleft()
            for xx in v[x]:
                if dp[i][xx] > dp[i][x] + 1:
                    dp[i][xx] = dp[i][x] + 1
                    q.append(xx)

    h = [0] * (n + 1)
    par = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = 1
        par[i] = i

    s = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s += dp[i][j]

    ans = [0] * (m + 1)

    for i in range(m, 0, -1):
        ans[i] = s
        x, y = p[i]
        x = find(par, x)
        y = find(par, y)
        if x == y:
            continue

        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dp[j][k] = min(dp[j][k], dp[j][x] + dp[y][k])
                dp[j][k] = min(dp[j][k], dp[j][y] + dp[x][k])

        s = 0
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                s += dp[j][k]

        union(par, h, x, y)

    for i in range(1, m + 1):
        print(ans[i])


if __name__ == "__main__":
    main()
