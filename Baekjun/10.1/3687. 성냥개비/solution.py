import math
import sys

input = sys.stdin.readline

T = int(input())

dp_max = [0] * (101)
dp_min = [math.inf] * (101)
min_map = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}

dp_max[2] = 1
dp_max[3] = 7

for i in range(4, 101):
    dp_max[i] = dp_max[i - 2] * 10 + 1

for key, val in min_map.items():
    dp_min[key] = val

dp_min[6] = 6

for i in range(8, 101):
    for key, val in min_map.items():
        val2 = dp_min[i - key] * 10 + val
        if i - key >= 0:
            dp_min[i] = min(dp_min[i], val2)

while T:
    T -= 1
    N = int(input())

    print(dp_min[N], dp_max[N])
