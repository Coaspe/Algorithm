import sys

input = sys.stdin.readline
ans = []

while True:
    n, money = map(float, input().rstrip().rsplit())
    n = int(n)

    if n == 0:
        break

    money = int(money * 100)

    candies = {}
    for _ in range(n):
        c, p = map(float, input().rstrip().rsplit())
        c = int(c)
        p = int(p * 100)
        candies[p] = max(candies.get(p, 0), c)

    # dp[i] = 돈이 i일때, 사탕 중 가장 높은 칼로리
    dp = [0] * (money + 1)

    # candies[0]: 칼로리, candies[1]: 가격
    for p, c in candies.items():
        for price in range(p, money + 1):
            dp[price] = max(dp[price], dp[price - p] + c)

    ans.append(dp[money])
print("\n".join(map(str, ans)))
