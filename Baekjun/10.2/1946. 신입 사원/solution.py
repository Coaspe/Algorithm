import sys

input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    grade = [0] * (n + 1)
    for i in range(n):
        a, b = map(int, input().split())
        grade[a] = b
    top = grade[1]
    for i in range(2, n + 1):
        if grade[i] < top:
            top = grade[i]
        else:
            n -= 1
    print(n)
