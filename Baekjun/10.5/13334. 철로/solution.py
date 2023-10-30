from heapq import heappush, heappop
from sys import stdin


def solution():
    input = stdin.readline

    N = int(input())
    arr = [sorted(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    D = int(input())
    hq = []

    ans = 0
    for a, b in arr:
        heappush(hq, a)

        while hq and hq[0] < b - D:
            heappop(hq)

        ans = max(ans, len(hq))

    print(ans)


if __name__ == "__main__":
    solution()
