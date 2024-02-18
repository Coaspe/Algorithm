S = list(input())

stack = []
answer = ""


def priority(x):
    if x == "+" or x == "-":
        return 1
    elif x == "*" or x == "/":
        return 2
    else:
        return 0


for s in S:
    if s.isalpha():
        answer += s
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while stack[-1] != "(":
            answer += stack.pop()
        stack.pop()
    else:
        while stack and priority(stack[-1]) >= priority(s):
            answer += stack.pop()
        stack.append(s)

while stack:
    answer += stack.pop()

print(answer)
