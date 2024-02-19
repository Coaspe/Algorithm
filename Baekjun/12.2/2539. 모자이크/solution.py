import sys


def solution():
    input = sys.stdin.readline
    _, __ = map(int, input().split())
    N = int(input())
    T = int(input())
    points = [tuple(map(int, input().split())) for _ in range(T)]
    points.sort(key=lambda x: x[1])
    MAXX = max(x for x, _ in points)

    def check(width):
        C = set()
        CNT = 0
        for i, (x, y) in enumerate(points):
            if (x, y) in C:
                continue

            CNT += 1

            if CNT > N:
                return False

            for j in range(i + 1, T):
                if points[j][1] - y + 1 > width:
                    break
                C.add(points[j])

        return True

    lo, hi = MAXX - 1, 10**5 + 1

    while hi > lo + 1:
        mid = (lo + hi) // 2

        if check(mid):
            hi = mid
        else:
            lo = mid

    print(hi)


if __name__ == "__main__":
    solution()
