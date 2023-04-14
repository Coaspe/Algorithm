import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
arr = [[5]*N for _ in range(N)]
s2d2 = []
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(N):
    s2d2.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

while K > 0:
    # 봄
    for i in range(N):
        for j in range(N):
            t_len = len(tree[i][j])
            for k in range(t_len):
                if arr[i][j] >= tree[i][j][k]:
                    arr[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 여름
                    for _ in range(k, t_len):
                        arr[i][j] += tree[i][j].pop() // 2
                    break

    # 가을
    for i in range(N):
        for j in range(N):
            for z in tree[i][j]:
                if z % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)
            # 겨울
            arr[i][j] += s2d2[i][j]
    K -= 1

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])
print(result)
