from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
C = list(map(int, input().split()))
P = [[i, C[i] % 2, int(C[i] % 2 == 0)] for i in range(N)]


def find(c):
    if P[c][0] != c:
        P[c][0] = find(P[c][0])
    return P[c][0]


def union(c1, c2):
    p1, p2 = find(c1), find(c2)

    if p1 == p2:
        return [-1, -1, -1]

    if p1 > p2:
        P[p1] = [p1, P[p1][1] + P[p2][1], P[p1][2] + P[p2][2]]
        P[p2] = [p1, 0, 0]
        return [p2, p1, (P[p1][1] + P[p2][1]) * (P[p1][2] + P[p2][2])]
    else:
        P[p2] = [p2, P[p1][1] + P[p2][1], P[p1][2] + P[p2][2]]
        P[p1] = [p2, 0, 0]
        return [p1, p2, (P[p1][1] + P[p2][1]) * (P[p1][2] + P[p2][2])]


from collections import defaultdict

dic = defaultdict(int)
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    r, np, v = union(a, b)

    if r == -1:
        print(ans)
        continue

    ans -= dic[r]
    dic[r] = 0

    ans += v - dic[np]
    dic[np] = v

    print(ans)
