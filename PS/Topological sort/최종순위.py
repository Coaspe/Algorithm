from collections import deque, defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 작년 순위
    n = int(input())
    rank = list(map(int, input().split()))
    indegree = [0]*(n+1)
    link = defaultdict(list)
    for i in range(n):
        link[rank[i]] = rank[i+1:]
        indegree[rank[i]] = i

    # 순위 역전
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a in link[b]:
            link[b].remove(a)
            link[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        else:
            link[a].remove(b)
            link[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
    print(link)
    print(indegree)
    # 시작 노드
    q = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)
    if not q:
        # 시작 노드 부재, 사이클
        print("IMPOSSIBLE")
        continue

    # 위상 정렬
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for i in link[v]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    if sum(indegree) > 0:
        # 사이클 존재
        print("IMPOSSIBLE")
    else:
        print(*ans)
