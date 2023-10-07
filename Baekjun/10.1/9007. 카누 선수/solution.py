import sys
from bisect import bisect_left

input = sys.stdin.readline
T = int(input())

while T:
    T -= 1
    K, N = map(int, input().split())
    classes = [list(map(int, input().split())) for _ in range(4)]
    c12 = []
    c34 = []

    for c1 in classes[0]:
        for c2 in classes[1]:
            c12.append(c1 + c2)

    for c3 in classes[2]:
        for c4 in classes[3]:
            c34.append(c3 + c4)

    c34.sort()

    ans = c12[0] + c34[0]

    def comp(tmp_ans):
        global ans
        if abs(K - ans) == abs(K - tmp_ans):
            ans = min(ans, tmp_ans)
        else:
            ans = min(ans, tmp_ans, key=lambda x: abs(K - x))

    for val in c12:
        idx = bisect_left(c34, K - val)
        tmp_ans = val + c34[idx]

        if idx == len(c34):
            comp(tmp_ans)
        else:
            comp(tmp_ans)
            if idx != 0:
                comp(val + c34[idx - 1])

        if ans == K:
            break

    print(ans)
