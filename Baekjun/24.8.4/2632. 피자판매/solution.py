from collections import defaultdict

S = int(input())
M, N = map(int, input().split())
MM = [int(input()) for _ in range(M)]
MS = sum(MM)
NN = [int(input()) for _ in range(N)]
NS = sum(NN)
dic_m = defaultdict(int)
dic_n = defaultdict(int)
dic_m[0] += 1
dic_n[0] += 1
ans = 0


def get(arr, n, dic, ss):
    for i in range(1, n + 1):
        ms = sum(arr[:i])
        s = 0

        while True:
            dic[ms] += 1

            if s != 0 and s + i - 1 != n - 1:
                dic[ss - ms] += 1

            if s + i - 1 == n - 1:
                break

            ms -= arr[s]
            ms += arr[s + i]
            s += 1


get(MM, M, dic_m, MS)
get(NN, N, dic_n, NS)

for k, i in dic_m.items():
    if dic_n[S - k]:
        ans += dic_n[S - k] * i

print(ans)
