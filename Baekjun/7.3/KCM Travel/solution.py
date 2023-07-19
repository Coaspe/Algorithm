import sys

INF = sys.maxsize
input = sys.stdin.readline

input()

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(K):
    departure, arrival, expense, time = map(int, input().split())
    graph[departure].append((arrival, expense, time))

arrival_expense = [[INF]*(M+1) for _ in range(N+1)]
arrival_expense[1][0] = 0
# 비용
for e in range(M+1):
    # 공항
    for d in range(1, N+1):
        if arrival_expense[d][e] == INF:
            continue
        temp_time = arrival_expense[d][e]
        for da, de, dt in graph[d]:
            next_expense = de + e
            if next_expense > M:
                continue
            arrival_expense[da][next_expense] = min(
                arrival_expense[da][next_expense], dt + temp_time)

result = min(arrival_expense[N])
print([result, 'Poor KCM'][result == INF])
