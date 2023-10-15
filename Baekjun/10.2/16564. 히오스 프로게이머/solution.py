N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]


def check(target):
    k = 0
    for x in X:
        k += max(0, target - x)
    return K >= k


l, r = min(X) - 1, 2_000_000_001

while r > l + 1:
    mid = (l + r) // 2

    if check(mid):
        l = mid
    else:
        r = mid

print(l)
