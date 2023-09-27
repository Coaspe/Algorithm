N, M, K = map(int, input().split())
candy = list(map(int, input().split()))

for i in range(N):
    candy[i] = [candy[i], 1]

parent = [i for i in range(N)]
rank = [0] * N


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union_by_rank(v1, v2):
    x = find(v1)
    y = find(v2)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union_by_rank(a, b)

for i in range(N):
    if parent[i] != i:
        p = find(i)
        candy[p][0] += candy[i][0]
        candy[p][1] += candy[i][1]


dp = [[0] * (K) for _ in range(N)]
dp[0][candy[0][1]] = candy[0][0]

for i in range(1, N):
    if parent[i] != i:
        continue
    for j in range(K - 1, candy[i][1] - 1, -1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - candy[i][1]] + candy[i][0])

# l = len(groups)
# dp = [[0] * K for _ in range(l)]

# for i in range(groups[0][0], K):
#     dp[0][i] = groups[0][1]

# for i in range(1, l):
#     weight, value = groups[i]

#     for j in range(K):
#         dp[i][j] = dp[i - 1][j]

#         if j >= weight:
#             dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i][j])

# print(dp[-1][-1])
