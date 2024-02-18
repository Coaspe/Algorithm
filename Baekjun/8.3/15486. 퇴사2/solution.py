from sys import stdin

n = int(stdin.readline())
t, p = [0], [0]
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    ti, pi = map(int, stdin.readline().split())
    t.append(ti)
    p.append(pi)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    fin_date = i + t[i] - 1

    if fin_date:
        continue
    dp[fin_date] = max(dp[i - 1] + p[i], dp[fin_date])

print(max(dp))
