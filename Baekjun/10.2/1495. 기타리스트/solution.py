N, S, M = map(int, input().split())
A = list(map(int, input().split()))
L = set([S])

for a in A:
    LT = set()
    for b in L:
        if b - a >= 0:
            LT.add(b - a)
        if a + b <= M:
            LT.add(a + b)
    L = LT

print(-1 if len(L) == 0 else max(L))
