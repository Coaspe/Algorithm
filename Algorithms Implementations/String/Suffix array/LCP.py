# Suffix
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
    lcp(sa, rank, n, S)

# Longest Common Prefix
def lcp(sa, rank, n, S):
    print(rank)
    # lcp array
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

MM(6,"banana")

# rank = 해당 index에서 시작하는 접미사 문자열의 rank(사전상 순서) 값을 나타냄
# SA = rank 값이 작은 접미사 문자열 순서대로 해당 문자열의 시작 index를 배열한 것
