T = int(input())
nums = [int(input()) for _ in range(T)] + [0, 0]

max_val = max(nums)
dp = [0] * (max_val + 1)
dp[0] = 1

for i in range(1, max_val + 1):
    dp[i] = sum([dp[i - 3], dp[i - 2], dp[i - 1]]) % 1_000_000_009

for i in nums[:-2]:
    print(dp[i])
