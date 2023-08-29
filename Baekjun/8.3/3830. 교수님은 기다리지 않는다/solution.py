from sys import stdin, setrecursionlimit

setrecursionlimit(10000)
input = stdin.readline


def find(x):
    if parents[x] == x:
        return x

    temp = find(parents[x])

    differ[x] += differ[parents[x]]
    parents[x] = temp

    return parents[x]


def union(x, y, t):
    a = find(x)
    b = find(y)

    # 더 작은 애한테 붙힌다.
    if a <= b:
        parents[b] = a
        # b - a = x - a + y - x - (y - b)
        differ[b] = differ[x] + t - differ[y]
    else:
        parents[a] = b
        differ[a] = differ[y] - t - differ[x]


def get(x, y):
    a = find(x)
    b = find(y)

    if a == b:
        print(differ[y] - differ[x])
    else:
        print("UNKNOWN")


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parents = list(range(n + 1))
    differ = [0] * (n + 1)

    for i in range(m):
        x = input().split()
        if x[0] == "!":
            union(int(x[1]), int(x[2]), int(x[3]))
        else:
            get(int(x[1]), int(x[2]))
