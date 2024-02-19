import heapq

N, K = map(int, input().split())
prev = int(input())
INF = 10**9
dist = [INF]

for idx in range(N - 1):
    new = int(input())
    dist.append(new - prev)
    prev = new

dist.append(INF)

left = [0, *range(N)]
right = [0, *range(2, N + 1), 0]

Q = []

for i in range(1, N):
    heapq.heappush(Q, (dist[i], i))

ans = 0

visit = [0] * (N + 1)
visit[0] = visit[-1] = 1

while Q and K > 0:
    D, idx = heapq.heappop(Q)

    if visit[idx]:
        continue

    l = left[idx]
    r = right[idx]

    ans += D
    K -= 1

    visit[l] = 1
    visit[r] = 1

    dist[idx] = dist[l] + dist[r] - D

    heapq.heappush(Q, (dist[idx], idx))

    left[idx] = left[l]
    right[idx] = right[r]

    left[right[idx]] = idx
    right[left[idx]] = idx

print(ans)
