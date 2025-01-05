from math import ceil


def can_remove_all_leaves(n, leaves, daily_fall, target_days):
    needed_boosts = 0
    for i in range(n):
        remaining = leaves[i] - daily_fall[i] * target_days

        if remaining <= 0:
            continue

        boosts = ceil(remaining / daily_fall[i])
        if boosts > target_days:
            return False
        needed_boosts += boosts

        if needed_boosts > target_days:
            return False

    return True


def solve_winter_coming():
    n = int(input())
    leaves = list(map(int, input().split()))
    daily_fall = list(map(int, input().split()))

    left = -1
    right = max(ceil(leaves[i] / daily_fall[i]) for i in range(n)) + 1

    while left + 1 < right:
        mid = (left + right) // 2
        if can_remove_all_leaves(n, leaves, daily_fall, mid):
            right = mid
        else:
            left = mid

    return right


print(solve_winter_coming())
