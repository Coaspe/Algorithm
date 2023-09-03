import math
from collections import defaultdict, deque
T = int(input())
while T:
    T -= 1
    # 공항의 수, 지원비용, 티켓정보의 수
    N, M, K = map(int, input().split())
    graph = defaultdict(list)
    # 해당 비용을 사용하여 노드로 갈 수 있는 가장 짧은 소요시간.
    dp = [[math.inf] * N for _ in range(M+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((c, d, v))
    q = deque([(0, 0, 0)])

    # 해당 cost로 해당 공항까지 갈 수 있는 최소 시간
    while q:
        time, cost, curr = q.popleft()
        if time > dp[cost][curr]:
            continue

        for c, d, v in graph[curr]:
            newCost = c + cost
            newTime = time + d
            if newCost <= M and newTime < dp[newCost][v]:
                for i in range(newCost, M+1):
                    if dp[i][v] > newTime:
                        dp[i][v] = newTime
                    else:
                        break
                q.append((newTime, newCost, v))

    print(dp[M][N-1] if dp[M][N-1] != math.inf else "Poor KCM")
