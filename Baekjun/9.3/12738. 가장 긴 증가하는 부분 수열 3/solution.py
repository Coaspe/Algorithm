from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

ans = []

for a in A:
    idx = bisect_left(ans, a)
    if idx == len(ans):
        ans.append(a)
    else:
        ans[idx] = a

print(len(ans))
