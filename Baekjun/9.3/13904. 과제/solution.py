from heapq import heappop, heappush

N = int(input())
hw = [[] for _ in range(1001)]
dis = 0

for _ in range(N):
    d, w = map(int, input().split())
    dis = max(dis, d)
    hw[d].append(w)


hq = []
ans = 0

for i in range(dis, 0, -1):
    for d in hw[i]:
        heappush(hq, -d)

    if hq:
        ans -= heappop(hq)

print(ans)
