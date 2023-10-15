N, M = map(int, input().split())
A = list(map(int, input().split()))


def check(T):
    cnt = 0
    for a in A:
        cnt += T // a
    return cnt >= M


l, r = 0, max(A) * M + 1

while r > l + 1:
    mid = (r + l) // 2
    if check(mid):
        r = mid
    else:
        l = mid

print(r)
