from bisect import bisect_left

N = int(input())
lcs = []

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

for _, b in arr:
    if not lcs:
        lcs.append(b)
        continue
    idx = bisect_left(lcs, b)
    if idx == len(lcs):
        lcs.append(b)
    else:
        lcs[idx] = b
print(N - len(lcs))
