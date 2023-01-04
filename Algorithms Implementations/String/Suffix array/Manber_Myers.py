# Suffix Array
def MM(n, S):
    sa = list(range(n))
    rank = list(map(ord, S))
    tmp = [0] * n
    k = 1
    while k <= n:
        cmp = [rank[i] << 20 | (1 + rank[i + k] if i + k < n else 0)
               for i in range(n)]
        sa.sort(key=lambda i: cmp[i])
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp[sa[i - 1]] < cmp[sa[i]])
        rank = tmp[:]
        k <<= 1
