import sys
INF = 1 << 60
MOD = 10**9 + 7  # 998244353
sys.setrecursionlimit(2147483647)
def input(): return sys.stdin.readline().rstrip()


def resolve():
    S = input() + '$'
    n = len(S)

    # Suffix array
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
    print(sa, rank)
    # lcp array
    lcp = [0] * n
    h = 0
    for i in range(n):
        j = sa[rank[i] - 1]
        if h:
            h -= 1
        while j + h < n and i + h < n and S[j + h] == S[i + h]:
            h += 1
        lcp[rank[i]] = h
    print(lcp)
    print(n * (n - 1) // 2 - sum(lcp))


resolve()
