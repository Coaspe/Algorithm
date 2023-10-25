# 백준 N-Queen

N = int(input())


def dfs(queen, row):
    count = 0
    if row == N:
        return 1

    for col in range(N):
        queen[row] = col

        for i in range(row):
            if queen[row] == queen[i]:
                break

            if abs(queen[row] - queen[i]) == row - i:
                break
        else:
            count += dfs(queen, row + 1)

    return count


print(dfs([0] * N, 0))
