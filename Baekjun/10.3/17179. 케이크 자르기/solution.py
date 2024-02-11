N, M, L = map(int, input().split())
S = [0] + [int(input()) for _ in range(M)] + [L]


def check(T, q):
    cnt = 0
    last = 0
    a = []
    for s in S:
        if s - last >= T:
            cnt += 1
            last = s
            a.append(s)

    return cnt >= q + 1


for _ in range(N):
    q = int(input())
    l, r = 0, L + 1

    ans = []
    while r > l + 1:
        mid = (l + r) // 2
        if check(mid, q):
            l = mid
        else:
            r = mid

    print(l)
