from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0


def insert(arr, val):
    idx = bisect_left(arr, val)
    if idx == len(arr):
        arr.append(val)
    else:
        arr[idx] = val


for i in range(N):
    l = [A[i]]
    d = [-A[i]]

    for j in range(i + 1, N):
        if A[j] > A[i]:
            insert(l, A[j])
        else:
            insert(d, -A[j])

    ans = max(ans, len(d) + len(l) - 1)
print(ans)
