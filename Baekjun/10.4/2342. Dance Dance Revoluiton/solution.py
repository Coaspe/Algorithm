nums = [0] + list(map(int, input().split()))[:-1]

N = len(nums)
# dp[i][left][right] = Minimum of Sum of power - [ith][left foot][right foot]
dp = [[[4 * N for _ in range(5)] for _ in range(5)] for _ in range(N)]
dp[0][0][0] = 0


def po(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a - b) == 2:
        return 4
    else:
        return 3


for i in range(1, N):
    a = nums[i]  # i-1 번째 값을 사용
    for left in range(5):
        for right in range(5):
            dp[i][a][right] = min(dp[i][a][right], dp[i - 1][left][right] + po(left, a))
            dp[i][left][a] = min(dp[i][left][a], dp[i - 1][left][right] + po(right, a))

print(min(map(min, dp[N - 1])))
