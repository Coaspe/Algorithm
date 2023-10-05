from heapq import heappop, heappush

N = int(input())
station = [list(map(int, input().split())) for _ in range(N)]

L, P = map(int, input().split())

if P >= L:
    print(0)
    exit(0)

q = []

station.sort(reverse=True)

loc = 0
ans = 0

while station:
    if station[-1][0] > P + loc:
        break
    a, b = station.pop()
    heappush(q, (-b, a))

while q:
    b, a = heappop(q)
    b = -b

    P += b
    ans += 1

    P -= max(0, a - loc)
    loc = max(loc, a)

    if loc + P >= L:
        break

    while station:
        if station[-1][0] > P + loc:
            break
        a, b = station.pop()
        heappush(q, (-b, a))

print(ans if loc + P >= L else -1)
