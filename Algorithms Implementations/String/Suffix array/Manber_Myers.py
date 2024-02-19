# Suffix Array
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


def MM2(n, s):
    t = 1
    suffix = list(range(n))
    g = [0] * (n + 1)  # 순위
    ng = [0] * (n + 1)  # 새로운 순위를 갱신할 때 이용

    for i in range(n):
        g[i] = ord(s[i])

    g[n] = -1
    ng[suffix[0]] = 0
    ng[n] = -1

    while t < n:
        suffix.sort(key=lambda x: (g[x], g[min(x + t, n)]))

        for i in range(1, n):
            p, q = suffix[i - 1], suffix[i]

            ng[q] = ng[p] + ((g[min(p + t, n)] != g[min(q + t, n)]) or (g[p] != g[q]))

        # # 처음 부터 정렬이 바로 되어 있을 때 바로 탈출 하기 위해서
        # if ng[n-1] == n-1:
        #     break

        t <<= 1
        g = ng[:]
    print(suffix)


MM2(6, "banana")
# https://m.blog.naver.com/jqkt15/222035128595
