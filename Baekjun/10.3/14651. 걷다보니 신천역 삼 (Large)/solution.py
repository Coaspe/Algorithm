import sys

input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    print(2 * 3 ** (n - 2) % 1000000009)
