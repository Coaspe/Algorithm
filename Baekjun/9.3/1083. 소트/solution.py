def find_lexicographically_largest(arr, max_swaps):
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, min(n, i + max_swaps + 1)):
            if arr[j] > arr[max_idx]:
                max_idx = j

        for j in range(max_idx, i, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            max_swaps -= 1

            if max_swaps == 0:
                break

        if max_swaps == 0:
            break

    return arr


n = int(input())
arr = list(map(int, input().split()))
max_swaps = int(input())

result = find_lexicographically_largest(arr, max_swaps)

print(" ".join(map(str, result)))
