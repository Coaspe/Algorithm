from collections import deque
T = int(input())


def bfs(h, w):
    q = deque([(h, w)])
    check = set([(h, w)])

    while q:
        r, c = q.popleft()

        for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0 <= row < H and 0 <= col < W and (row, col) not in check and M[row][col] != '*':
                charToint = ord(M[row][col])
                global tt
                if M[row][col] == '$':
                    global ans
                    ans += 1
                # Upper case
                elif 65 <= charToint <= 90:
                    if M[row][col].lower() not in keys:
                        continue
                    tt += 1
                # Lower case
                elif 97 <= charToint <= 122:
                    keys.add(M[row][col])
                    tt += 1

                M[row][col] = '.'
                check.add((row, col))
                q.append((row, col))


while T:

    T -= 1

    H, W = map(int, input().split())
    M = [list(input()) for _ in range(H)]
    keys = set(list(input()))
    start_points = []

    for h in range(H):
        for w in range(W):
            if M[h][w] == '.' and (h == H - 1 or w == W - 1 or h == 0 or w == 0):
                start_points.append((h, w))

    ans = 0

    while True:
        tmp = ans
        tt = 1
        while tt:
            tt -= 1
            for h, w in start_points:
                bfs(h, w)

        if tmp == ans:
            break

    print(ans)
