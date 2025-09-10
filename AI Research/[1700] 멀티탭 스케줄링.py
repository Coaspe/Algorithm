from bisect import bisect_left

N, K = map(int, input().split())

KK = list(map(int, input().split()))

M = {}
for i, k in enumerate(KK):
    M[k] = M.get(k, []) + [i]


S = set()
i = 0
ans = 0
for i in range(K):
    if KK[i] in S:
        continue

    if len(S) < N:
        S.add(KK[i])
    else:
        mx = -1
        mxk = -1
        for s in S:
            idx = bisect_left(M[s], i)
            if idx == len(M[s]):
                mxk = s
                break
            if M[s][idx] > mx:
                mx = M[s][idx]
                mxk = s

        S.remove(mxk)
        S.add(KK[i])
        ans += 1
print(ans)
