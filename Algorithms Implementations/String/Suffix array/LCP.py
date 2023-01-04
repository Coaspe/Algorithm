def lcp(sa, rank, n, S):
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

    print(n * (n - 1) // 2 - sum(lcp))
