# Suffix array
def MM(n, S):
    sa = list(range(n))
    rank = list(map(ord, S))
    tmp = [0] * n
    k = 1

    while k <= n:
        # rank[i] << 20는 그룹 랭크를 의미
        # 1 + rank[i + k] ->
        # 1을 더해주는 이유는 rank가 0인 것과 i + k < n 인 경우를 구분하기 위해서이다.
        # rank[i + k]를 사용해서 전체 시간 복잡도가 n(logn)^2이 되는 것이다.
        cmp = [rank[i] << 20 | (1 + rank[i + k] if i + k < n else 0) for i in range(n)]

        # rank를 사용해서 suffix array 정렬
        sa.sort(key=lambda i: cmp[i])

        tmp[sa[0]] = 0

        # 새로운 rank 생성
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp[sa[i - 1]] < cmp[sa[i]])

        rank = tmp[:]
        k <<= 1

    lcp(sa, rank, n, S)


# Longest Common Prefix
def lcp(sa, rank, n, S):
    # lcp array
    lcp = [0] * n
    k = 0

    # 가장 긴 suffix부터 시작
    for i in range(n):
        # j: 현재 접미사보다 랭크가 1 낮은 (sa 배열에서 바로 앞)인 접미사의 문자열 S 안에서의
        j = sa[rank[i] - 1]

        if k:
            k -= 1

        while j + k < n and i + k < n and S[j + k] == S[i + k]:
            k += 1

        lcp[rank[i]] = k

    return lcp


MM(6, "banana")

# rank = 해당 index에서 시작하는 접미사 문자열의 rank(사전상 순서) 값을 나타냄
# SA = rank 값이 작은 접미사 문자열 순서대로 해당 문자열의 시작 index를 배열한 것
