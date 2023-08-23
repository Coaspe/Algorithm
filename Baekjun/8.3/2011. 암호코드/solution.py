num = [int(i) for i in input()]

if num[0] == 0:
    print(0)
    exit(0)

N = len(num)

dp = [0] * N

if N == 1:
    print(N)
    exit(0)

dp[0] = 1
dp[1] = int(10 <= num[0] * 10 + num[1] <= 26) + int(num[1] != 0)

for i in range(2, len(num)):
    if num[i] > 0:
        dp[i] = dp[i - 1]
    if 10 <= num[i - 1] * 10 + num[i] <= 26:
        dp[i] += dp[i - 2]

print(dp[-1] % 1000000)
