N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def dfs(c, aa):
    if c == 1:
        print(aa[0][0])
        return

    aaa = [[]]

    for i in range(0, c, 2):
        for j in range(0, c, 2):
            x = sorted([aa[i][j], aa[i + 1][j], aa[i][j + 1], aa[i + 1][j + 1]])
            if len(aaa[-1]) < c // 2:
                aaa[-1].append(x[-2])
            else:
                aaa.append([x[-2]])

    dfs(c // 2, aaa)


dfs(N, A)
