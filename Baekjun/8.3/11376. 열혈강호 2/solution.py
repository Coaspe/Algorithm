from collections import deque

# 입력 받기
N, M = map(int, input().split())
tasks_input = [list(map(int, input().split())) for _ in range(N)]

# 각 근로자별로 연결 가능한 작업 번호만 따로 추출
# 예: tasks[i] = [가능한 작업1, 가능한 작업2, ...]
tasks = []
for row in tasks_input:
    # row[0] = 이 근로자가 할 수 있는 작업 수 (사용하지 않아도 무방)
    # row[1:] = 실제 작업 번호들
    _, *arr = row
    tasks.append(arr)

# -- 왼쪽 집합(L) 노드 개수: 근로자 한 명을 2개 노드로 분할 => 2*N개 --
#    오른쪽 집합(R) 노드 개수: 작업(M개)

L = 2 * N  # 왼쪽 집합(근로자) 전체 노드 수
R = M  # 오른쪽 집합(작업) 노드 수

# 그래프 인접 리스트 (왼쪽 노드 -> 연결된 오른쪽 노드 목록)
# 왼쪽 정점 번호 범위: 0 ~ (2N - 1)
# 오른쪽 정점 번호 범위: 0 ~ (M - 1)
adj = [[] for _ in range(L)]

# 각 근로자 i에 대해:
#  - i (왼쪽 노드) -> 가능한 작업들
#  - i+N (왼쪽 노드) -> 똑같은 작업들
#    이렇게 두 개로 분할해 연결해줍니다.
for i in range(N):
    for t in tasks[i]:
        # 작업 t는 1 <= t <= M 이라고 가정 → 0-based로 쓰려면 t-1
        t_idx = t - 1
        # 근로자 i의 '첫 번째 노드' (i)와 연결
        adj[i].append(t_idx)
        # 근로자 i의 '두 번째 노드' (i+N)와 연결
        adj[i + N].append(t_idx)

# ------------------ Hopkroft-Karp 알고리즘 구현 ------------------ #
# pairU[u] : 왼쪽 정점 u와 매칭된 오른쪽 정점 번호 (없으면 -1)
# pairV[v] : 오른쪽 정점 v와 매칭된 왼쪽 정점 번호 (없으면 -1)
# dist[u]  : BFS 단계에서 왼쪽 정점 u의 거리(레이어)

pairU = [-1] * L
pairV = [-1] * R
dist = [-1] * L


def bfs():
    """왼쪽 정점들에 대해 BFS로 레벨 그래프(거리 dist)를 구성"""
    queue = deque()
    # 1) 매칭이 안 된(=자유로운) 왼쪽 정점들을 큐에 넣고, 거리 dist[u] = 0
    for u in range(L):
        if pairU[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float("inf")

    # dist_nil = 매칭되지 않은 오른쪽 정점과 연결되는 '가장 가까운 레벨' 추적
    dist_nil = float("inf")

    # 2) BFS 진행
    while queue:
        u = queue.popleft()
        # 현재 정점 u의 거리가 아직 dist_nil(최단 매칭 거리)보다 작다면 탐색
        if dist[u] < dist_nil:
            for v in adj[u]:  # u와 연결된 오른쪽 정점들
                w = pairV[v]  # v와 매칭된 왼쪽 정점
                if w == -1:
                    # 오른쪽 v가 아직 매칭되지 않았다면,
                    # dist_nil까지의 거리가 하나 더 늘어났다고 보면 됨
                    return True
                else:
                    # v가 이미 w와 매칭되어 있다면,
                    # w가 더 깊은 레벨로 갈 수 있는지 확인
                    if dist[w] == float("inf"):
                        dist[w] = dist[u] + 1
                        queue.append(w)

    # dist_nil이 갱신되었다면, 매칭을 늘릴 수 있는 경로가 존재함
    return False


def dfs(u):
    """레벨 그래프(dist)를 기반으로, 왼쪽 정점 u에서 시작하는 증대 경로를 탐색"""
    if u != -1:
        for v in adj[u]:
            w = pairV[v]
            # w == -1 이면 오른쪽 정점 v가 아직 매칭되지 않았으므로 곧장 연결 가능
            # w != -1 이면, dist[w]가 dist[u] + 1인 레벨 그래프의 구조를 만족해야 함
            if w == -1 or (w != -1 and dist[w] == dist[u] + 1 and dfs(w)):
                pairU[u] = v
                pairV[v] = u
                return True
        # 증대 경로를 찾지 못했다면, 이 정점은 다음에 다시 방문할 필요 X
        dist[u] = float("inf")
        return False
    return True


# Hopkroft-Karp 본체
matching = 0
# BFS로 레벨 그래프 구성 후, DFS로 증대 경로를 찾을 수 없을 때까지 반복
while bfs():
    # 매칭되지 않은(=자유로운) 왼쪽 정점들 각각에 대해 DFS 시도
    for i in range(L):
        if pairU[i] == -1:
            if dfs(i):
                matching += 1

# matching = 최대 매칭의 크기 = 근로자들이 맡을 수 있는 작업 개수의 최댓값
print(matching)
