from sys import maxsize


def find_closest_to_zero(N, s):
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + s[i - 1]

    indexed_prefix_sum = [(prefix_sum[i], i) for i in range(N + 1)]

    indexed_prefix_sum.sort()

    min_diff = maxsize
    ans_diff = None
    best_l, best_r = 0, 0

    for i in range(1, N + 1):
        diff = abs(indexed_prefix_sum[i][0] - indexed_prefix_sum[i - 1][0])
        if diff < min_diff:
            min_diff = diff
            l = indexed_prefix_sum[i - 1][1]
            r = indexed_prefix_sum[i][1]
            if l > r:
                ans_diff = indexed_prefix_sum[i - 1][0] - indexed_prefix_sum[i][0]
            else:
                ans_diff = indexed_prefix_sum[i][0] - indexed_prefix_sum[i - 1][0]
            best_l = min(l, r) + 1
            best_r = max(l, r)

    return ans_diff, best_l, best_r


N = int(input())
s = list(map(int, input().split()))

min_diff, L, R = find_closest_to_zero(N, s)

print(min_diff)
print(L, R)
