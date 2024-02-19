n = int(input())

arr = list(map(int, input().split()))
map_num = {1: 0, 2: 0, 3: 0}

for num in arr:
    map_num[num] += 1

# dp[three][two][one] = 초밥이 1,2,3개 남은 접시가 각각 one,two,three개 남아있을 때,
# 다 먹을떄까지 필요한 operation 횟수의 기대값.
dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

for three in range(n + 1):
    for two in range(n + 1):
        for one in range(n + 1):
            zero = n - three - two - one

            if zero == n or zero < 0:
                continue

            val = 1
            if three > 0:
                val += (three / n) * dp[three - 1][two + 1][one]
            if two > 0:
                val += (two / n) * dp[three][two - 1][one + 1]
            if one > 0:
                val += (one / n) * dp[three][two][one - 1]

            dp[three][two][one] = val / (1 - 1.0 * zero / n)

print(dp[map_num[3]][map_num[2]][map_num[1]])
