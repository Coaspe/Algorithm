T = int(input())

while T:
    T -= 1
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    price = int(input())

    dp = [0] * (price + 1)
    dp[0] = 1

    for i in range(1, len(coins)):
        for j in range(coins[i], price + 1):
            dp[j] += dp[j - coins[i]]

    print(dp[-1])
