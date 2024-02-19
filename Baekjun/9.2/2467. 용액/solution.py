import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

result = [float("inf"), float("inf")]

for idx in range(N - 1):
    low = idx + 1
    high = N - 1

    while low + 1 < high:
        mid = (low + high) // 2

        if arr[mid] + arr[idx] < 0:
            low = mid
        else:
            high = mid

    temp = []

    if abs(arr[idx] + arr[low]) < abs(arr[idx] + arr[high]):
        temp = [arr[idx], arr[low]]
    else:
        temp = [arr[idx], arr[high]]

    if abs(sum(temp)) < abs(sum(result)):
        result = temp

    if sum(result) == 0:
        break


print(*result)
