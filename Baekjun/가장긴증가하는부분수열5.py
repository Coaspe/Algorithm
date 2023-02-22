import bisect as bs

n = int(input())
nums = list(map(int, input().split()))
dp = [0]*n
# 문제의 조건에 음수가 포함되므로 최저를 0이 아닌 -무한대로 설정해준다.
cp = []

for i in range(n):
    if not cp or nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp)-1
    else:
        dp[i] = bs.bisect_left(cp, nums[i])
        cp[dp[i]] = nums[i]
print(len(cp))
# 역추적
max_idx, ans = max(dp), []
for i in range(n-1, -1, -1):
    if dp[i] == max_idx:
        ans.append(nums[i])
        max_idx = dp[i] - 1
print(*ans[::-1])
