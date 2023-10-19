from sys import stdin

input = stdin.readline

N = int(input())


def dfs(n):
    if n == 1:
        return "*"

    stars = dfs(n // 3)

    L = []

    for star in stars:
        L.append(star * 3)

    for star in stars:
        L.append(star + " " * (n // 3) + star)

    for star in stars:
        L.append(star * 3)

    return L


print("\n".join(dfs(N)))
