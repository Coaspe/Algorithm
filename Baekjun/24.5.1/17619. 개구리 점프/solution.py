import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, Q = map(int, input().split())
W = []

group = [0] * N
index = [0] * N

for i in range(N):
    l = list(map(int, input().split()))
    l.append(i)
    W.append(l)

W.sort()
WW = []

cur = 0

for idx, (a, b, c, i) in enumerate(W):
    index[i] = idx
    if WW and a <= WW[-1][1]:
        WW[-1][1] = max(WW[-1][1], b)
    else:
        cur += 1
        WW.append([a, b, c, i])

    group[idx] = cur

for s, e in [tuple(map(int, input().split())) for _ in range(Q)]:
    s -= 1
    e -= 1
    print(int(group[index[s]] == group[index[e]]))
