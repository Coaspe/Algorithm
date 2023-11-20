import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(99999)

    V, E = map(int, input().split())

    discovered = [0] * (V + 1)
    cnt = 1
    ans = [0] * (V + 1)
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    def dfs(root, now):
        nonlocal cnt
        discovered[now] = cnt
        num = cnt

        cnt += 1
        child = 0
        for nxt in G[now]:
            if discovered[nxt] == 0:
                child += 1
                low = dfs(0, nxt)
                num = min(num, low)
                if not root and low >= discovered[now]:
                    ans[now] = 1
            else:
                num = min(num, discovered[nxt])

        if root and child >= 2:
            ans[now] = 1

        return num

    for i in range(1, V + 1):
        if discovered[i] == 0:
            dfs(1, i)

    print(sum(ans))
    print(*[i for i in range(1, V + 1) if ans[i] == 1])


if __name__ == "__main__":
    solution()
