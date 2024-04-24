from math import sqrt

N, M = map(int, input().split())

B = [list(input()) for _ in range(N)]
ans = -1


def dfs(i, j, num, i_g, j_g):
    num += B[i][j]

    i_num = int(num)
    i_num_r = int(num[::-1])

    sqr = sqrt(i_num)
    sqr_r = sqrt(i_num_r)

    global ans

    if int(sqr) == sqr and i_num > ans:
        ans = i_num
    if int(sqr_r) == sqr_r and i_num_r > ans:
        ans = i_num_r

    new_i = i + i_g
    new_j = j + j_g

    if 0 <= new_i < N and 0 <= new_j < M:
        dfs(new_i, new_j, num, i_g, j_g)


for i in range(N):
    for j in range(M):
        if int(sqrt(int(B[i][j]))) == sqrt(int(B[i][j])):
            ans = max(ans, int(B[i][j]))

        for i_g in range(N):
            for j_g in range(M):
                if i_g == j_g == 0:
                    continue

                dfs(i, j, "", i_g, j_g)
                dfs(i, j, "", -i_g, -j_g)
                dfs(i, j, "", i_g, -j_g)
                dfs(i, j, "", -i_g, j_g)

print(ans)
