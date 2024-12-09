N, M = map(int, input().split())

xyspsp = [list(map(int, input().split())) for _ in range(N)]

from math import ceil


def ps(target):
    remain = M

    for x, y, sm, pm, sv, pv in xyspsp:
        need = target * x - y

        if need <= 0:
            continue

        # m의 개수
        n = ceil(need / sm) + 1
        min_d = float("inf")

        for i in range(n + 1):
            min_d = min(min_d, i * pm + ceil((need - i * sm) / sv) * pv)

        remain -= min_d

        if remain < 0:
            return False

    return True


l, r = -1, M + 1
while r > l + 1:
    target = (l + r) // 2

    if ps(target):
        l = target
    else:
        r = target

print(l)
