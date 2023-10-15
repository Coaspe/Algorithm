from sys import stdin

input = stdin.readline
N, D = map(int, input().split())

SC = []

for _ in range(N):
    a, b, d = map(int, input().split())
    if d >= b - a or b > D:
        continue
    SC.append([a, b, d])

dp = [i for i in range(D + 1)]

SC.sort()

for i in range(len(SC)):
    a, b, d = SC[i]
    dp[b] = min(dp[b], dp[a] + d)
    for j in range(b + 1, D + 1):
        dp[j] = min(dp[j], dp[b] + j - b)

print(dp[-1])
