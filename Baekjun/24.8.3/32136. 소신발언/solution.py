def calculate_time(a, i):
    n = len(a)
    max_time = 0
    for j in range(n):
        max_time = max(max_time, abs(i - j) * a[j])
    return max_time


def ternary_search(a):
    left, right = 0, len(a) - 1

    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        time1 = calculate_time(a, mid1)
        time2 = calculate_time(a, mid2)

        if time1 > time2:
            left = mid1 + 1
        else:
            right = mid2 - 1

    min_time = float("inf")
    for i in range(left, right + 1):
        min_time = min(min_time, calculate_time(a, i))

    return min_time


N = int(input())
a = list(map(int, input().split()))

print(ternary_search(a))
