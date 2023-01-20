import sys
import heapq
import collections
n, m = map(int, sys.stdin.readline().rstrip().split())

answer = []
graph = collections.defaultdict(list)
inDegree = [0]*(n+1)
queue = []


for i in range(m):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    graph[first].append(second)
    inDegree[second] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str, answer)))
