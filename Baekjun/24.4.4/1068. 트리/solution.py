def solution():
    N = int(input())
    tree = list(map(int, input().split()))
    removed = int(input())
    G = [[] for _ in range(N)]
    root = []
    ans = 0

    for i, val in enumerate(tree):

        if val == removed or i == removed:
            continue
        if val == -1:
            root.append(i)
            continue

        G[val].append(i)

    def dfs(n):
        if not G[n]:
            nonlocal ans
            ans += 1
            return

        for next_node in G[n]:
            dfs(next_node)

    for r in root:
        dfs(r)

    print(ans)


if __name__ == "__main__":
    solution()
