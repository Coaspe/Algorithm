def counting(arr, K):
    m = max(K)
    C = [0] * (m + 1)
    for a in arr:
        C[a] += 1
    for i in range(1, m + 1):
        C[i] += C[i - 1]
    result = [0] * len(arr)
    for a in arr:
        result[C[a] - 1] = a
        C[a] -= 1
    return result
