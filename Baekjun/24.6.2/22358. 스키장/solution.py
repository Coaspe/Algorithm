from sys import maxsize

N, M, K, S, T = map(int, input().split())
inf = maxsize
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))

dp = [-inf] * N

dp[S - 1] = 0
for k in range(K + 1):

    for i in range(N):
        for b, c in G[i]:
            dp[b] = max(dp[b], dp[i] + c)

    if k == K:
        break

    tdp = dp[:]

    for i in range(N):
        for b, _ in G[i]:
            tdp[i] = max(tdp[i], dp[b])

    dp = tdp

print(dp[T - 1] if dp[T - 1] >= 0 else -1)
