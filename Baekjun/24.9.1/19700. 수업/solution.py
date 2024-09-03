from bisect import bisect_left
from sys import stdin

input = stdin.readline
N = int(input())

ghq = []
c = [tuple(map(int, input().split())) for _ in range(N)]
c.sort(reverse=True)
ans = []


for h, k in c:
    idx = bisect_left(ans, -k)

    if idx == len(ans):
        ans.append(-2)
    else:
        ans[idx] -= 1
print(len(ans))
