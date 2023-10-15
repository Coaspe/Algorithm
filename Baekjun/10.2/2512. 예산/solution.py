N = int(input())
A = list(map(int, input().split()))
L = int(input())
A.sort()

l, r = 0, A[-1] + 1


def check(target):
    acc = 0
    for a in A:
        if a > target:
            acc += target
        else:
            acc += a
    return acc <= L


while r > l + 1:
    mid = (r + l) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)
