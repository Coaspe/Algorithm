from bisect import bisect_left


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dic_BToA = {b: a for a, b in zip(range(N), B)}
    dp = []
    dp2 = [-1] * (N + 1)

    for a in A:
        b = dic_BToA[a]
        if not dp or dp[-1] < b:
            dp.append(b)
            dp2[b] = len(dp) - 1
        else:
            idx = bisect_left(dp, b)
            dp[idx] = b
            dp2[b] = idx

    L = len(dp)
    print(L)

    ans = []
    L -= 1

    for i in range(N, -1, -1):
        if dp2[i] == L:
            L -= 1
            ans.append(B[i])

    print(*sorted(ans))


if __name__ == "__main__":
    solution()
