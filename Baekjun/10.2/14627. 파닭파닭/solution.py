S, C = map(int, input().split())
P = [int(input()) for _ in range(S)]


def check(T):
    cnt = 0
    for p in P:
        cnt += p // T
    return cnt >= C


l, r = 0, max(P) + 1

while r > l + 1:
    mid = (l + r) // 2

    if check(mid):
        l = mid
    else:
        r = mid

print(sum(P) - (C * l))
