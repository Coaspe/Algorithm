for _ in range(3):
    N = int(input())
    coins = {}
    target = 0

    for _ in range(N):
        a, b = map(int, input().split())
        coins[a] = b
        target += a * b

    if target & 1:
        print(0)
        continue

    target //= 2
    dp = [1] + [0] * target

    for c in coins:
        for m in range(target, c - 1, -1):
            if dp[m - c]:
                for j in range(coins[c]):
                    if m + c * j <= target:
                        dp[m + c * j] = 1

    print(dp[target])
