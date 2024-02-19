from heapq import heappop, heappush, heapify

N = int(input())
arr = [int(input()) for _ in range(N)]

heapify(arr)

ans = 0

while len(arr) > 1:
    x, y = heappop(arr), heappop(arr)
    ans += x + y
    heappush(arr, x + y)

print(ans)
