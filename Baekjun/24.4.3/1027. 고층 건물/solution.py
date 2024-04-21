def solution():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    def cal(i, j):
        scope = (A[j] - A[i]) / (j - i)
        b = A[i] - scope * i

        for k in range(i + 1, j):
            y = scope * k + b
            if A[k] >= y:
                return 0

        return 1

    for i in range(N):
        tmp_ans = 0
        for j in range(N):
            l, s = max(i, j), min(i, j)

            if l == s:
                continue

            tmp_ans += cal(s, l)

        ans = max(ans, tmp_ans)
    print(ans)


if __name__ == "__main__":
    solution()
