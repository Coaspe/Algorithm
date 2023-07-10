# 둘 사이에 둘 중에 하나보다 큰 녀석이 있으면 안 된다.
N = int(input())
# (height, cnt)
stack = []
ans = 0
nums = [int(input()) for _ in range(N)]

for i in range(N):
    while stack and nums[i] > stack[-1][0]:
        ans += stack.pop()[1]

    if not stack:
        stack.append((nums[i], 1))
        continue

    # 현재 스택의 끝값과 같을 때
    if stack[-1][0] == nums[i]:
        cnt = stack.pop()[1]
        ans += cnt

        if stack:
            ans += 1

        stack.append((nums[i], cnt+1))
    else:
        stack.append((nums[i], 1))
        ans += 1

print(ans)
