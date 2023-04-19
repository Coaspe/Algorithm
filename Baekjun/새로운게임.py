# N, K = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# # i 번째 말의 위치
# info = [-1] * K

# # (r, c) 위치에 쌓여 있는 말들의 index
# # 위치 : [indices]
# file = {}

# for i in range(K):
#     r, c, d = map(int, input().split())

#     info[i] = (r, c, d)

#     if (r, c) in file:
#         file[(r, c)].append(i)
#     else:
#         file[(r, c)] = [i]

# def next_p(r, c, d):
#     if d == 0:
#         c += 1
#     elif d == 1:
#         r -= 1
#     elif d == 2:
#         c -= 1
#     elif d == 3:
#         r += 1
#     return (r, c)

# def move_child(prev, next, move_p):
#     prev_f, next_f = file[prev], file[next]
#     move_i = prev_f.find(move_p)
#     prev_f = prev_f[:move_i+1]
#     next_f.extends(prev_f[move_i+1:])

# while True:
#     for i in range(K):
#         r1, c1, d = info[i]
#         r2, c2 = next_p(r1, c1, d)

#         # White
#         if board[r][c] == 0:
#             info[i] = (r, c)
#             idx = file[]
#         # Red
#         elif board[r][c] == 1:
#             pass
#         # Blue
#         elif board[r][c] == 2:
#             pass

x = {
    1: []
}

print(x[1])
xx = x[1]
xx.append(1)
print(x[1])
