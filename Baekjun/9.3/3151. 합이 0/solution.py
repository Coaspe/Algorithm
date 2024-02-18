answer = 0
n = int(input())
nums = sorted(list(map(int, input().split())))

for i in range(n - 2):
    left = i + 1
    right = n - 1
    target = -nums[i]
    max_idx = n

    if target < 0:
        break

    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum > target:
            right -= 1
        elif two_sum < target:
            left += 1
        else:
            if nums[left] == nums[right]:
                answer += right - left
            else:
                if max_idx > right:
                    max_idx = right
                    while max_idx >= 0 and nums[max_idx - 1] == nums[right]:
                        max_idx -= 1
                answer += right - max_idx + 1
            left += 1

print(answer)
