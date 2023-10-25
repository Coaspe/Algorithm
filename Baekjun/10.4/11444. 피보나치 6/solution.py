from sys import setrecursionlimit, stdin


def solution():
    input = stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    answer = 0

    def dfs(node):
        if not G[node]:
            return 0

        ans = []

        for child, w in G[node]:
            ans.append(dfs(child) + w)

        nonlocal answer
        answer = max(answer, sum(sorted(ans)[-2:]))

        return max(ans)

    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))

    dfs(0)
    print(answer)


if __name__ == "__main__":
    setrecursionlimit(10**5)
    solution()
