from sys import stdin

input = stdin.readline

N, M, K = map(int, input().split())
min_alch = float("inf")
max_alch = 0
B = []

for _ in range(K):
    v, c = map(int, input().split())
    max_alch = max(c, max_alch)
    min_alch = min(c, min_alch)
    B.append([v, c])
B.sort(key=lambda x: -x[0])


def check(T):
    acc = 0

    TN = N
    for i in range(K):
        k, c = B[i]
        if c <= T:
            acc += k
            TN -= 1
            if not TN:
                break
    return acc >= M and not TN


O = max_alch + 1
l, r = min_alch - 1, O

while r > l + 1:
    mid = (l + r) // 2

    if check(mid):
        r = mid
    else:
        l = mid

print(r if r != O else -1)
