from sys import setrecursionlimit

setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

dp = [[[-1] * 3 for _ in range(N)] for _ in range(2)]


def dfs(node, dir, left):
    if node == N - 1:
        dp[dir][node][left] = 0

    if dp[dir][node][left] != -1:
        return dp[dir][node][left]

    next_node = node - A[node]
    next_node_reversed = node + A[node]

    if dir:
        next_node, next_node_reversed = next_node_reversed, next_node

    if 0 <= next_node < N:
        val = dfs(next_node, dir, left)
        if val > -1:
            dp[dir][node][left] = val + 1

    if left:
        next_node, next_node_reversed = next_node_reversed, next_node
        if 0 <= next_node < N:
            val = dfs(next_node, dir ^ 1, left - 1)
            if val > -1:
                dp[dir][node][left] = max(dp[dir][node][left], val + 1)

    return dp[dir][node][left]


print(dfs(0, 1, 2))
