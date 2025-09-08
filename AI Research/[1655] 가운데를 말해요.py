from heapq import heappush, heappop
from sys import stdin

input = stdin.readline


def maintain_median():
    left_heap = []
    right_heap = []

    for _ in range(int(input())):
        n = int(input())

        if left_heap and -left_heap[0] > n:
            heappush(left_heap, -n)
            n = -heappop(left_heap)

        if right_heap and right_heap[0] < n:
            heappush(right_heap, n)
            n = heappop(right_heap)

        if len(left_heap) <= len(right_heap):
            heappush(left_heap, -n)
        else:
            heappush(right_heap, n)

        print(-left_heap[0] if len(left_heap) >= len(right_heap) else right_heap[0])


maintain_median()
