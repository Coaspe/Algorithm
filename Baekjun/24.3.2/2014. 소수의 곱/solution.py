import heapq

k, n = map(int, input().split())
prime = list(map(int, input().split()))
heap = []

for idx, v in enumerate(prime):
    heapq.heappush(heap, (v, idx))


for i in range(n - 1):
    min_val, idx = heapq.heappop(heap)
    for index, v in enumerate(prime):

        if index > idx:
            break

        heapq.heappush(heap, (min_val * v, index))

print(heapq.heappop(heap)[0])
