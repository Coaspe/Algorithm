from sys import stdin, setrecursionlimit


def solution():
    input = stdin.readline
    setrecursionlimit(10**6)

    N = int(input())
    G = [[] for _ in range(N + 1)]

    # dp[i][0]: i번 노드가 얼리어답터가 아닐 때
    # dp[i][1]: i번 노드가 얼리어답터일 때
    dp = [[0, 0] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    def dfs(n):
        visited[n] = True
        dp[n][1] = 1
        for child in G[n]:
            if not visited[child]:
                dfs(child)
                dp[n][0] += dp[child][1]
                dp[n][1] += min(dp[child])

    dfs(1)

    print(min(dp[1]))


if __name__ == "__main__":
    solution()
