K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

l, r = 1, max(arr)

while r >= l:
    mid = (l + r) // 2
    tmp = 0
    for i in arr:
        tmp += i // mid
    if tmp < N:
        r = mid-1
    elif tmp >= N:
        l = mid+1
print(r)
