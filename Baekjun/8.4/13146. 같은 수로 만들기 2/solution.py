import sys

input = sys.stdin.readline

N = int(input())

stack = [int(input())]
ans = 0

for _ in range(N - 1):
    num = int(input())

    if stack[-1] == num:
        continue

    if len(stack) > 1 and stack[-2] > stack[-1] and num > stack[-1]:
        while len(stack) > 1 and stack[-2] > stack[-1] and num > stack[-1]:
            ans += (stack[-2] if num > stack[-2] else num) - stack[-1]
            if num == stack[-2]:
                stack.pop()
            stack.pop()

    stack.append(num)

while len(stack) > 1:
    ans += abs(stack[-2] - stack.pop())

print(ans)
