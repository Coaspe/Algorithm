import sys

input = sys.stdin.readline

N = int(input())
LH = []
RH = []
LP = []
RP = []
D = []
for p in range(N):
    h, d = input().split()
    h = int(h)
    D.append(d)

    if d == "L":
        LH.append(h)
        LP.append(p)
        continue

    RH.append(h)
    RP.append(p)

LH.sort()
RH.sort()

if not LH or not RH:
    print(N)
    exit(0)

if LH[-1] == N:
    d = "L"
    LH.pop()
else:
    d = "R"
    RH.pop()

ans = 1
for p in range(N):
    if D[p] != d:
        continue

    A = [0] * N
    A[p] = N

    l = r = 0

    for i in range(p):
        if D[i] == "R":
            A[i] = RH[r]
            r += 1

    for i in range(N - 1, p, -1):
        if D[i] == "L":
            A[i] = LH[l]
            l += 1

    height = -1
    cnt = 0

    for i in range(p):
        if D[i] == "R":
            height = A[i]
            continue

        while l < len(LH) and LH[l] < height:
            l += 1

        if l < len(LH) and LH[l] > height:
            l += 1
            cnt += 1

    height = -1
    for i in range(N - 1, p, -1):
        if D[i] == "L":
            height = A[i]
            continue

        while r < len(RH) and RH[r] < height:
            r += 1

        if r < len(RH) and RH[r] > height:
            r += 1
            cnt += 1

    ans = max(ans, cnt + 1)

print(ans)
