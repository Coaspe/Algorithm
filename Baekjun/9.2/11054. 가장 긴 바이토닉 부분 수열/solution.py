N = int(input())
arr = list(map(int, input().split()))

front = [1] * N

for i in range(N):
    max_val = 0
    for j in range(i - 1, -1, -1):
        if arr[j] < arr[i]:
            max_val = max(max_val, front[j])
    front[i] += max_val

back = [1] * N

for i in range(N - 1, -1, -1):
    max_val = 0
    for j in range(i + 1, N):
        if arr[j] < arr[i]:
            max_val = max(max_val, back[j])
    back[i] += max_val

ans = max(map(sum, zip(front, back))) - 1

print(ans)
