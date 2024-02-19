import sys

input = sys.stdin.readline
N, H = map(int, input().split())
heights = [0] * (H + 2)

for i in range(N):
    val = int(input())
    if i % 2:
        heights[H + 1] -= 1
        heights[H - val + 1] += 1
    else:
        heights[1] += 1
        heights[val + 1] -= 1

for i in range(2, H + 1):
    heights[i] += heights[i - 1]

heights = heights[1 : H + 1]
min_val = min(heights)

print(min_val, heights.count(min_val))
