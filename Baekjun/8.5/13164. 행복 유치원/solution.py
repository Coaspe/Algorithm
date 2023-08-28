import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

array = []
for i in range(1, n):
    array.append(kids[i] - kids[i - 1])

array.sort()
print(sum(array[: n - k]))
