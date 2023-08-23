import bisect as bs

N = int(input())
nums = list(map(int, input().split()))
cp = []

for i in range(N):
    if not cp or nums[i] > cp[-1]:
        cp.append(nums[i])
    else:
        idx = bs.bisect_left(cp, nums[i])
        cp[idx] = nums[i]
print(len(cp))
