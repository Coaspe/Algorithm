import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

answer = 0
cnt = 0

while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)


input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
rank = [0 for _ in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])


def find(v):
    if Vroot[v] != v:
        Vroot[v] = find(Vroot[v])
    return Vroot[v]


def union_by_rank(p1, p2):
    # rank가 큰 트리에 작은 트리를 붙입니다.
    if rank[p1] > rank[p2]:
        Vroot[p2] = p1
    elif rank[p1] < rank[p2]:
        Vroot[p1] = p2
    else:  # 만약 rank가 같다면 임의로 p1 트리에 p2 트리를 붙입니다.
        Vroot[p2] = p1
        rank[p1] += 1


answer = 0
for s, e, w in Elist:
    p1 = find(s)
    p2 = find(e)
    if p1 != p2:
        union_by_rank(p1, p2)
        answer += w


print(answer)
