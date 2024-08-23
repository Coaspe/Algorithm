from heapq import heappop, heappush
from sys import stdin


def solution():
    input = stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))

    ans = [0] * M

    def djik(end_arr):
        inf = 10000 * 1000
        hq = [(0, end_arr[0][0])]
        dp = [inf] * N
        dp[end_arr[0][0]] = 0

        while hq:
            cost, node = heappop(hq)

            if cost > dp[node]:
                continue

            for new_node, next_cost in G[node]:
                new_cost = cost + next_cost

                if dp[new_node] > new_cost:
                    dp[new_node] = new_cost
                    heappush(hq, (new_cost, new_node))

        for _, end, index in end_arr:
            ans[index] = dp[end]

    query = []
    for i in range(M):
        a, b = sorted(map(int, input().split()))
        a -= 1
        b -= 1
        query.append((a, b, i))

    query.sort()

    end_arr = []
    for a, b, i in query:
        if not end_arr or end_arr[0][0] == a:
            end_arr.append((a, b, i))
        else:
            djik(end_arr)
            end_arr = [(a, b, i)]

    if end_arr:
        djik(end_arr)

    for i in ans:
        print(i)


if __name__ == "__main__":
    solution()
