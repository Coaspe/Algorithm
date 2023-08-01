from collections import deque
N = int(input())
S = deque(list(input()))

stack = []
inStack = 0
while S:
    c = S.popleft()

    if c == ')':
        if inStack:
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
            inStack -= 1
        else:
            stack.append(c)
    elif c == '(':
        stack.append(c)
        inStack += 1
    else:
        stack.append(c)

print(''.join(stack))
