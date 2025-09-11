from sys import stdin
from bisect import bisect_right

input = stdin.readline
A, B = map(int, input().split())
N = int(input())

aa, bb = [], []

for i in range(N):
    a, b = map(int, input().split())
    aa.append((a, i + 1))
    bb.append((b, i + 1))


aa.sort()
if B > A:
    print(*[-1, -1])
    exit(0)

ans_diff = float("inf")
ans = "No"


def set_ans(idx, b):
    global ans, ans_diff
    a, af = aa[idx]
    new_diff = abs(A - B - b - a)
    if A - B - b - a < 0 and new_diff < ans_diff:
        ans_diff = new_diff
        ans = (af, b_index)


for a, a_index in aa:
    if A - B - a < 0 and abs(A - B - a) <= ans_diff:
        ans_diff = abs(A - B - a)
        ans = (a_index, -1)

for b, b_index in bb:
    if A - B - b < 0:
        if abs(A - B - b) <= ans_diff:
            ans_diff = abs(A - B - b)
            ans = (-1, b_index)
        continue

    a_idx = bisect_right(aa, A - B - b, key=lambda x: x[0])
    if a_idx == N:
        a_idx -= 1
    a, a_index = aa[a_idx]
    if a_index == b_index:
        a_m = a_idx - 1
        a_p = a_idx + 1

        if a_m >= 0:
            set_ans(a_m, b)
        elif a_p < N:
            set_ans(a_p, b)
    else:
        set_ans(a_idx, b)

print("No" if ans == "No" else f"{ans[0]} {ans[1]}")
