import math

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_costs = [math.inf] * N
ans = math.inf
# 해당 마스크 -> 모두 1인 마스크까지 가는 데 소모되는 cost의 최솟값을 저장
check = [math.inf] * (1 << 16)


def processing(x):
    return 0 if x == 'N' else 1


status = list(map(processing, list(input())))
least = int(input())
s_off = least - status.count(1)


def dfs(bits, left):

    if left == 0:
        return 0

    if check[bits] != math.inf:
        return check[bits]

    for i in range(N):
        if bits & (1 << (N - i - 1)):
            for j in range(N):
                if not bits & (1 << (N - j - 1)):
                    check[bits] = min(
                        check[bits], arr[i][j] + dfs(bits | (1 << (N - j - 1)), left - 1))

    return check[bits]


status_decimal = 0

for i in range(len(status)):
    status_decimal += status[i] * (1 << (len(status) - 1 - i))

if s_off > 0:
    ans = dfs(status_decimal, s_off)
    print(ans if ans != math.inf else -1)
else:
    print(0)
