import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 입력
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 종이의 수들 중 최대값
max_val = max(map(max, board))

# 최대값 변수
answer = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
# dfs의 경로모양이 ㅗ, ㅜ, ㅓ, ㅏ를 제외한 모든 모양들을 만들 수 있음


def dfs(x, y, dsum, cnt):
    global answer
    # 중요(백트래킹 부분) - 만약 현재까지의 최대값이 현재 경로까지의 합 + 종이 수들 중 최대값 * 남은 경로 횟수보다 크다면
    # 남은 경로에서 종이수들중 최대값만 나와서 더해준다고 해도 현재 최대값보다 커지지 못하는 경우는 미리 가지치기
    if answer >= dsum + max_val * (4 - cnt):
        return
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        answer = max(answer, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]

        # 만약 움직인 좌표가 올바른 범위 안에 있고 방문한적이 없다면
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # ㅗ, ㅜ, ㅓ, ㅏ 모양에 대한 처리
            if cnt == 2:
                # 방문 처리
                visited[nx][ny] = True
                # dfs(이동좌표, 현재까지 경로의 수의 합, 지나온 칸 개수)
                dfs(x, y, dsum + board[nx][ny], cnt + 1)
                # 방문 제거
                visited[nx][ny] = False

            # ㅗ, ㅜ, ㅓ, ㅏ 모양을 제외한 모양들에 대한 처리
            # 방문 처리
            visited[nx][ny] = True
            # dfs(이동좌표, 현재까지 경로의 수의 합, 지나온 칸 개수)
            dfs(nx, ny, dsum + board[nx][ny], cnt+1)
            # 방문 제거
            visited[nx][ny] = False


# 종이를 반복하면서
for i in range(n):
    for j in range(m):
        # 현재 좌표 방문처리
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        # 현재 좌표 방문처리 해제
        visited[i][j] = False

print(answer)
