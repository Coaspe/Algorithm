def solution():
    N = int(input())
    A = [[x for x in input()] for _ in range(N)]

    def dfs(r, c):
        for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
            if 0 <= row < N and 0 <= col < N and A[row][col] == "1":
                A[row][col] = "0"
                dfs(row, col)
                nonlocal tmp
                tmp += 1

    ans = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == "1":
                tmp = 1
                A[i][j] = "0"
                dfs(i, j)
                ans.append(tmp)

    print(len(ans))

    for i in sorted(ans):
        print(i)


if __name__ == "__main__":
    solution()
