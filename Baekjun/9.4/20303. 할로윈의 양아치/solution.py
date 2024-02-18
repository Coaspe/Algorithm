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


dp = [0] * (K)

for i in range(N):
    if parent[i] != i:
        continue
    for j in range(K - 1, candy[i][1] - 1, -1):
        dp[j] = max(dp[j], dp[j - candy[i][1]] + candy[i][0])
        print(i, j)
        print(*dp)

print(dp[-1])
