N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
sticker = []
for _ in range(K):
    R, C = map(int, input().split())
    sticker.append([list(map(int, input().split())) for _ in range(R)])

for i in range(K):
    block = sticker[i]
    flag = False
    for direction in range(4):
        if flag:
            break

        for _ in range(direction):
            block = list(zip(*block[::-1]))

        for r in range(N):
            if flag:
                break
            for c in range(M):
                if board[r][c] != 0:
                    continue
                if flag:
                    break

                one_flag = False
                tmp = set()

                for br in range(len(block)):
                    for bc in range(len(block[0])):
                        if block[br][bc]:
                            new_r, new_c = r+br, c+bc
                            if 0 <= new_r < N and 0 <= new_c < M and not board[new_r][new_c]:
                                tmp.add((new_r, new_c))
                            else:
                                one_flag = True
                                break

                    if one_flag:
                        break

                if not one_flag:
                    flag = True
                    for r2, c2 in tmp:
                        board[r2][c2] = 1


ans = 0

for r in range(N):
    for c in range(M):
        ans += int(board[r][c] == 1)
print(ans)
