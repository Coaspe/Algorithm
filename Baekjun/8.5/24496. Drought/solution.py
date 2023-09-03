def solve():
    n = int(input())
    h = [int(i) for i in input().split()]
    cnt = 0

    for _ in range(2):
        for i in range(1, n - 1):
            if h[i] > h[i - 1]:
                dif = h[i] - h[i - 1]
                h[i] -= dif
                h[i + 1] -= dif
                cnt += dif * 2

        if h[n - 1] > h[n - 2]:
            return -1

        h = h[::-1]

    if h[0] < 0:
        return -1

    return cnt


# 4 3 2 1
# 1 2 3 4
for i in range(int(input())):
    print(solve())
