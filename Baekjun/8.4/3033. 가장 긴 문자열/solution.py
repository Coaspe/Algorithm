def lcp(sa, rank, n, S):
    lcp = [0] * n
    k = 0

    for i in range(n):
        j = sa[rank[i] - 1]

        if k:
            k -= 1

        while j + k < n and i + k < n and S[j + k] == S[i + k]:
            k += 1

        lcp[rank[i]] = k

    return lcp


def MM(n, S):
    sa = list(range(n))
    rank = list(map(ord, S))
    tmp = [0] * n
    k = 1

    while k <= n:
        cmp = [rank[i] << 20 | (1 + rank[i + k] if i + k < n else 0) for i in range(n)]

        sa.sort(key=lambda i: cmp[i])

        tmp[sa[0]] = 0

        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp[sa[i - 1]] < cmp[sa[i]])

        rank = tmp[:]
        k <<= 1

    return lcp(sa, rank, n, S)


max_val = max(MM(int(input()), input()))

if max_val >= 2:
    print(max_val)
else:
    print(0)
