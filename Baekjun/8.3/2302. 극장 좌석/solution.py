N, M = int(input()), int(input())

if N <= 2:
    print(N)
    exit(0)

nums = [0] + [int(input()) for _ in range(M)] + [N + 1]
arr = [nums[i] - nums[i - 1] - 1 for i in range(1, len(nums))]

L = max(arr)

dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, L + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1

for i in arr:
    ans *= dp[i]

print(ans)
