from sys import stdin

input = stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
for i in range(N - 1, -1, -1):
    if A[i] == N:
        N -= 1
print(N)
