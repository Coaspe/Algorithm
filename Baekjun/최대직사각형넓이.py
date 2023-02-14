import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


def calculateArea(heights, start: int, end: int) -> int:
    if start > end:
        return 0
    min_index = start
    for i in range(start, end + 1):
        if heights[min_index] > heights[i]:
            min_index = i
    return max(
        heights[min_index] * (end - start + 1),
        calculateArea(heights, start, min_index - 1),
        calculateArea(heights, min_index + 1, end),
    )


while True:
    heights = list(map(int, input().split()))
    if len(heights) == 1 and heights[0] == 0:
        break

    print(calculateArea(heights, 0, len(heights) - 1))
