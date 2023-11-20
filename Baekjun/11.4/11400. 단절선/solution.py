import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)

    V, E = map(int, input().split())

    discovered = [0] * (V + 1)
    cnt = 1
    ans = []
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    def dfs(now, parent):
        nonlocal cnt
        discovered[now] = cnt
        num = cnt

        cnt += 1

        for nxt in G[now]:
            if nxt == parent:
                continue

            if discovered[nxt] == 0:
                low = dfs(nxt, now)
                num = min(num, low)
                if low > discovered[now]:
                    ans.append((min(now, nxt), max(now, nxt)))
            else:
                num = min(num, discovered[nxt])

        return num

    for i in range(1, V + 1):
        if discovered[i] == 0:
            dfs(1, -1)

    print(len(ans))

    for a, b in sorted(ans):
        print(a, b)


if __name__ == "__main__":
    solution()
