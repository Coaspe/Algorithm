T = int(input())
k = 0
coin = [1, 10, 25]

dp = [10**15 + 1 for _ in range(100)]
dp[0] = 0

for c in coin:
    for i in range(c, 100):
        dp[i] = min(dp[i], dp[i - c] + 1)

while T:
    T -= 1
    x = int(input())
    ans = 0

    while x:
        ans += dp[x % 100]
        x //= 100

    print(ans)
