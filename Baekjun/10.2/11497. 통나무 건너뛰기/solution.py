from sys import stdin

input = stdin.readline
from collections import deque

T = int(input())

while T:
    T -= 1
    N = int(input())
    A = sorted(map(int, input().split()))
    ans = deque()

    while A:
        ans.append(A.pop())
        if A:
            ans.appendleft(A.pop())

    ans = list(ans)
    val = abs(ans[-1] - ans[0])

    for i in range(1, N):
        val = max(val, abs(ans[i] - ans[i - 1]))

    print(val)
