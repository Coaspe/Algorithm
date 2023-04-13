import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
nut_tmp = [list(map(int, input().split())) for _ in range(N)]
nut = [[5]*N for _ in range(N)]
# r, c, 나이, 생사
trees = [[deque() for _ in range(N)] for _ in range(N)]
tree_s = set()

for _ in range(M):
    r, c, l = list(map(int, input().split()))
    r -= 1
    c -= 1
    trees[r][c].append((l, 1))
    tree_s.add((r, c))

for r, c in tree_s:
    trees[r][c] = deque(sorted(list(trees[r][c])))
    print(trees[r][c])
print(trees)
while K:
    for r, c in tree_s:
        for idx, t in enumerate(trees[r][c]):
            l, a = t
            if nut[r][c] >= l:
                nut[r][c] -= l
                trees[r][c][idx] = (l+1, a)
            else:
                trees[r][c][idx] = (l, 0)

    for r, c in list(tree_s):
        tmp = deque()
        for l, a in trees[r][c]:
            if a == 0:
                nut[r][c] += l // 2
            else:
                tmp.append((l, a))

        trees[r][c] = tmp

        if len(trees[r][c]) == 0:
            tree_s.remove((r, c))
        else:
            for l, a in trees[r][c]:
                if l % 5 == 0:
                    for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r-1, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1):
                        if 0 <= row < N and 0 <= col < N:
                            print(trees[row][col])
                            trees[row][col].appendleft((1, 1))
                            tree_s.add((row, col))

    for r in range(N):
        for c in range(N):
            nut[r][c] += nut_tmp[r][c]
    K -= 1

ans = 0
for r, c in tree_s:
    ans += len(trees[r][c])
print(ans)
