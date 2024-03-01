import sys

input = sys.stdin.readline


def dfs(cnt, s, path):
    global result

    if cnt == 7:
        if s > 0:
            result += 1
        return

    if 7 - cnt + s < 0:
        return

    for r, c in pos:
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (
                0 <= nr < 5
                and 0 <= nc < 5
                and (nr, nc) not in pos
                and path | 1 << (5 * nr + nc) not in checked
            ):
                pos.add((nr, nc))
                checked.add(path | 1 << (5 * nr + nc))
                dfs(cnt + 1, s + seat[nr][nc], path | 1 << (5 * nr + nc))
                pos.remove((nr, nc))


seat = [list(map(lambda x: 1 if x == "S" else -1, input().rstrip())) for _ in range(5)]
result = 0
checked = set()
pos = set()

for i in range(5):
    for j in range(5):
        pos.add((i, j))
        checked.add(1 << (5 * i + j))
        dfs(1, seat[i][j], 1 << (5 * i + j))
        pos = set()

print(result)
