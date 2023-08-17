from sys import stdin

n = int(stdin.readline())
t, p = [], []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    ti, pi = map(int, stdin.readline().split())
    t.append(ti)
    p.append(pi)

k = 0
for i in range(n):
    k = max(k, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])

print(max(dp))
