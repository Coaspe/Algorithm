N, M = map(int, input().split())
A = list(map(int, input().split()))


def check(target):
    cnt = 1
    acc = 0
    for a in A:
        acc += a

        if acc > target:
            cnt += 1
            acc = a

    return cnt <= M


l, r = max(A) - 1, 1_000_000_000

while r > l + 1:
    mid = (l + r) // 2

    if check(mid):
        r = mid
    else:
        l = mid

print(r)
