import heapq
import sys

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    G[a].append([b, c])
    G[b].append([a, c])

# dp[i][j] => i에 도착했을 때, j개의 도로를 지웠다고 가정한다면 얻을 수 있는 최소 시간
# MAX = int(1e6)
MAX = sys.maxsize
dp = [[MAX] * (K + 1) for _ in range(N)]

dp[0][0] = 0

hq = [(0, 0, 0)]

while hq:
    dist, k, node = heapq.heappop(hq)

    if dist > dp[node][k]:
        continue

    for next_node, next_dist in G[node]:
        new_dist = next_dist + dist
        if dp[next_node][k] > new_dist:
            dp[next_node][k] = new_dist
            heapq.heappush(hq, (new_dist, k, next_node))

        if k < K and dp[next_node][k + 1] > dist:
            dp[next_node][k + 1] = dist
            heapq.heappush(hq, (dist, k + 1, next_node))

print(min(dp[-1]))
