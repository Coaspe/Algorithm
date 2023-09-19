import sys


def input():
    return sys.stdin.readline().rstrip()


def solve():
    two_sum = set()

    for i in range(N):
        for j in range(i + 1):
            two_sum.add(A[i] + A[j])

    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if A[i] - A[j] in two_sum:
                return A[i]


N = int(input())

A = [int(input()) for _ in range(N)]

A.sort()
print(solve())
