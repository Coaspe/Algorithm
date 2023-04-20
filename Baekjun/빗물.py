H, W = map(int, input().split())
block = list(map(int, input().split()))
stack = []
answer = 0
for i in block:
    if not stack or stack[-1] <= i:
        stack.append(i)
    else:
        # 계산
        s = min(stack[0], stack[-1])
        for ii in stack[1:-1]:
            answer += (s-ii)
        stack = [stack[-1], i]

if stack:
    for ii in stack[1:]:
        answer += (stack[0]-ii)

print(answer)
