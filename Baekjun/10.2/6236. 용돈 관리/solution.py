from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
A = list(int(input()) for _ in range(N))


def check(mid):
    money = 0
    cnt = 0

    for a in A:
        if money - a < 0:
            cnt += 1
            money = mid
        money -= a

    return cnt


l, r = max(A) - 1, sum(A) + 1

while r > l + 1:
    mid = (r + l) // 2
    R = check(mid)
    if R <= M:
        r = mid
    else:
        l = mid
print(r)
