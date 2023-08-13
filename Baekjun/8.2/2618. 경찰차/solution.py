import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def findDP(dp, case1, case2, car1, car2, n):
    if dp[car1][car2] != -1:
        return dp[car1][car2]

    if car1 == n or car2 == n:
        return 0

    nextCase = max(car1, car2) + 1

    car1Dis = abs(case1[car1][0] - case1[nextCase][0]) + abs(
        case1[car1][1] - case1[nextCase][1]
    )
    car2Dis = abs(case2[car2][0] - case2[nextCase][0]) + abs(
        case2[car2][1] - case2[nextCase][1]
    )

    result1 = car1Dis + findDP(dp, case1, case2, nextCase, car2, n)
    result2 = car2Dis + findDP(dp, case1, case2, car1, nextCase, n)

    dp[car1][car2] = min(result1, result2)

    return dp[car1][car2]


def pathPrint(dp, case1, case2, car1, car2, n):
    if car1 == n or car2 == n:
        return 0

    nextCase = max(car1, car2) + 1

    car1Dis = abs(case1[car1][0] - case1[nextCase][0]) + abs(
        case1[car1][1] - case1[nextCase][1]
    )
    car2Dis = abs(case2[car2][0] - case2[nextCase][0]) + abs(
        case2[car2][1] - case2[nextCase][1]
    )

    result1 = car1Dis + dp[nextCase][car2]
    result2 = car2Dis + dp[car1][nextCase]

    if result1 < result2:
        print(1)
        pathPrint(dp, case1, case2, nextCase, car2, n)
    else:
        print(2)
        pathPrint(dp, case1, case2, car1, nextCase, n)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    # 1번이 i번째 케이스, 2번이 j번째 케이스일때

    dp = [[-1] * (m + 2) for _ in range(m + 2)]
    startLocCar1 = [(1, 1)]
    startLocCar2 = [(n, n)]
    case = [tuple(map(int, input().split())) for _ in range(m)]
    case1 = startLocCar1 + case
    case2 = startLocCar2 + case
    print(findDP(dp, case1, case2, 0, 0, m))
    pathPrint(dp, case1, case2, 0, 0, m)
    print(dp)
