from collections import defaultdict

UNVISITED = -1  # constant


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.g = defaultdict(list)
        self.id = 0

    def addEdge(self, u, v):
        self.g[u].append(v)

    # 메인 알고리즘
    def findSCCs(self):
        ids = [UNVISITED] * self.v  # 노드 수만큼 -1
        low = [UNVISITED] * self.v  # 노드 수만큼 -1

        onStack = [False] * self.v  # 노드 수만큼 False
        stack = []  # dfs

        for i in range(self.v):
            if ids[i] == UNVISITED:  # 노드 i가 처음이면 dfs
                self.dfs(i, low, ids, onStack, stack)
                
        return low  # low-link 값이 같은 것끼리 SCC를 만든다.

    # 깊이 우선 탐색
    def dfs(self, at, low, ids, onStack, stack):
        ids[at] = low[at] = self.id
        self.id += 1  # id 부여

        onStack[at] = True  # 현재 노드 visited
        stack.append(at)

        for to in self.g[at]:
            if ids[to] == UNVISITED:  # 처음 사용하는 노드라면
                self.dfs(to, low, ids, onStack, stack)  # 연결된 노드로 dfs
                low[at] = min(low[at], low[to])  # low-link 업데이트
            elif onStack[to] == True:  # 스택에 있으면
                low[at] = min(low[at], ids[to])  # low-link 업데이트

        # SCC 결과 출력하기
        w = UNVISITED
        
        if low[at] == ids[at]:
            print("Strongly Connected Components: ", end="")
            while w != at:
                w = stack.pop()
                print(f"Node {w}", end=" ")
                onStack[w] = False
            print()

    def __str__(self):
        return self.print()

    def print(self):
        for vertice, edge in self.g.items():
            print(f"{vertice} ->", *edge)


if __name__ == "__main__":
    g = Graph(8)  # 8 vertices
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(3, 4)
    g.addEdge(3, 7)
    g.addEdge(4, 5)
    g.addEdge(5, 0)
    g.addEdge(5, 6)
    g.addEdge(6, 0)
    g.addEdge(6, 2)
    g.addEdge(6, 4)
    g.addEdge(7, 3)
    g.addEdge(7, 5)

    # g.print()
    g.findSCCs()


""" 결과

Strongly Connected Components: Node 2 Node 1 Node 0 
Strongly Connected Components: Node 6 Node 5 Node 4 
Strongly Connected Components: Node 7 Node 3 

"""