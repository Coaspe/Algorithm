N = int(input())
MAX = 1000001
dp = [MAX] * (N + 1)
dp[1] = 0
if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 1

for i in range(4, N + 1):
    dp[i] = 1
    x = dp[i - 1]
    if i % 2 == 0:
        x = min(x, dp[i // 2])
    if i % 3 == 0:
        x = min(x, dp[i // 3])
    dp[i] += x

ans = [N]

while N != 1:
    y = N - 1
    if N % 2 == 0:
        y = min(y, N // 2, key=lambda x: dp[x])
    if N % 3 == 0:
        y = min(y, N // 3, key=lambda x: dp[x])
    N = y
    ans.append(N)

print(dp[-1])
print(*ans)
