from math import log2

x, y = map(int, input().split())
one_sum = [0 for _ in range(60)]

for i in range(1, 60):
    one_sum[i] = one_sum[i - 1] * 2 + 2 ** (i - 1)


def count(num):
    cnt = 0
    bit_num = bin(num)[2:]
    N = len(bit_num)

    for i in range(N):
        if num <= 0:
            break
        if bit_num[i] == "1":
            power = int(log2(num))
            cnt += num - 2**power + 1
            cnt += one_sum[power]
            num -= 2**power
    return cnt


print(count(y) - count(x - 1))
