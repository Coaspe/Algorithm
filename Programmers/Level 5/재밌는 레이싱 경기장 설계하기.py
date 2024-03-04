def solution(heights):
    N = len(heights)
    heights.sort()
    OFFSET = N // 2

    min_list = []

    for i in range(OFFSET):
        min_list.append(heights[OFFSET + i] - heights[i])

    if N % 2:
        min_list.append(heights[-1] - heights[OFFSET])

    min_list.sort()

    return min_list[N % 2]
