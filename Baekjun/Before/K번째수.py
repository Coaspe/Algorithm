N = int(input())
K = int(input())

s = 1
e = min(10 ** 9, N * N)
ans = 0


def check(mid):
    total = 0

    for i in range(1, N+1):
        total += min(mid, mid // i)
    return K <= total


while e >= s:
    mid = (e + s) // 2
    ans = 0
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
