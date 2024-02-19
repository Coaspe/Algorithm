from collections import defaultdict
import sys

input = sys.stdin.readline


def dfs(n):
    if data[n] != 0:
        return data[n]

    data[n] = dfs(n // p) + dfs(n // q)
    return data[n]


if __name__ == "__main__":
    n, p, q = map(int, input().split())
    data = defaultdict(int)
    data[0] = 1

    print(dfs(n))
