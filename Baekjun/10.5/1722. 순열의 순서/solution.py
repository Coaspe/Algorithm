# BOJ 1722. 순열의 순서

import sys
from math import factorial

input = sys.stdin.readline


def solution():
    N = int(input())
    nums = list(map(int, input().split()))

    if nums[0] == 1:
        k = nums[1]
        answer = []
        check = [False] * (N + 1)

        for i in range(N):
            for j in range(1, N + 1):
                if check[j]:
                    continue

                F = factorial(N - i - 1)

                if F < k:
                    k -= F
                else:
                    answer.append(j)
                    check[j] = True
                    break

        print(*answer)

    else:
        answer = 1
        nums = nums[1:]
        check = [False] * (N + 1)

        for i in range(N):
            for j in range(1, nums[i]):
                if not check[j]:
                    answer += factorial(N - i - 1)

            check[nums[i]] = True

        print(answer)


if __name__ == "__main__":
    solution()
