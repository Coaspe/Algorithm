N, K, D = map(int, input().split())

boxex = [list(map(int, input().split())) for _ in range(K)]


def check(mid):
    acc = 0
    for a, b, c in boxex:
        if mid - a >= 0:
            acc += (min(b, mid) - a) // c + 1
    return acc >= D


l, r = 1, N

while r > l + 1:
    mid = (r + l) // 2

    if check(mid):
        r = mid
    else:
        l = mid

print(r)
