def dfs(bomb):
    global n, result
    while bomb:
        x, y = bomb.pop()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx == 0 or nx == n-1) or (ny == 0 or ny == n-1):
                if arr[nx][ny] == 0:
                    break
        else:
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if (nx == 0 or nx == n-1) or (ny == 0 or ny == n-1):
                    arr[nx][ny] -= 1
            result += 1
    return


n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
bomb = []  # 폭탄
result = 0
if n > 4:  # 테두리와 인접하지 않는 칸은 모두 폭탄이라고 생각
    result += (n-4)**2
for i in range(n):
    for j in range(n):
        if i == 1 or i == n-2:
            if arr[i][j] == "#":
                bomb.append((i, j))
            else:
                arr[i][j] = int(arr[i][j])
        elif 1 < i < n-2:
            if j == 1 or j == n-2:
                bomb.append((i, j))
            else:
                if arr[i][j] != "#":
                    arr[i][j] = int(arr[i][j])
        else:
            if arr[i][j] != '#':
                arr[i][j] = int(arr[i][j])
dfs(bomb)
print(result)
