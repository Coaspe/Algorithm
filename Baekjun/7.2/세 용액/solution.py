# 세 용액

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cand = [10**10, 0, 0, 0]
for i in range(0, n - 2):
    l, r = i + 1, n - 1
    while (l < r):
        sum = arr[i] + arr[l] + arr[r]
        if abs(sum) < cand[0]:
            cand[0] = abs(sum)
            cand[1] = arr[i]
            cand[2] = arr[l]
            cand[3] = arr[r]
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1
        else:
            print(cand[1], cand[2], cand[3])
            exit(0)

print(cand[1], cand[2], cand[3])
