from sys import setrecursionlimit

setrecursionlimit(10**5)


def solve():
    n = int(input())
    fee = [0] + [int(input()) for _ in range(n)]

    memo = {}  # 메모이제이션을 위한 딕셔너리

    def opt(square, jumplen):
        if square < 1 or square > n:
            return float("inf")

        if square == n:
            return fee[n]

        if (square, jumplen) in memo:
            return memo[(square, jumplen)]

        min_cost = min(
            opt(square - jumplen, jumplen), opt(square + jumplen + 1, jumplen + 1)
        )

        memo[(square, jumplen)] = min_cost + fee[square]

        return memo[(square, jumplen)]

    print(opt(2, 1))


solve()
