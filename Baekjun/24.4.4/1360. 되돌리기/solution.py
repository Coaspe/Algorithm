stack = []
for _ in range(int(input())):
    op, c, t = input().split()
    t = int(t)

    if op == "type":
        stack.append((t, stack[-1][1] + c if stack else c))
    else:
        c = int(c)
        for idx, (a, b) in enumerate(stack):
            if a >= t - c:
                stack.append((t, stack[idx - 1][1] if idx > 0 else ""))
                break
        else:
            stack.append((t, stack[-1][1] if stack else ""))


print(stack[-1][1])
