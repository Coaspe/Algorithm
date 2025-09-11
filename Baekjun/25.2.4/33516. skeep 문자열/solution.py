N = int(input())
s = input()

stack = []
ans = 0

for i in range(N):
    stack.append(s[i])
    L = len(stack)
    while L >= 5 and "".join(stack[-5:]) == "skeep":
        ans += 1

        for _ in range(5):
            stack.pop()

        if stack and stack[-1] == "s":
            stack.append("k")
        elif L >= 2 and "".join(stack[-2:]) == "sk":
            stack.append("e")
        elif L >= 3 and "".join(stack[-3:]) == "ske":
            stack.append("e")
        elif L >= 4 and "".join(stack[-4:]) == "skee":
            stack.append("p")

print(ans)
