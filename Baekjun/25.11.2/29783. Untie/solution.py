for t in range(int(input())):
    S = list(input())
    N = len(S)
    ans = 0

    i = 0

    while i < N:
        j = i
        while (j + 1) < N and S[j + 1] == S[j]:
            j += 1

        l = j - i + 1
        ans += l // 2

    if S[0] == S[-1]:
        f = 0

        while f < N and S[f] == S[0]:
            f += 1

        b = 0

        while b < N and S[-1 - b] == S[0]:
            b += 1

        merge_len = f + b

        ans -= f // 2 + b // 2
        ans += merge_len // 2

    print(ans)
