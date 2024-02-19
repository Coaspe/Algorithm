from collections import defaultdict

N = int(input())
F = []
start = 3 * 30 + 1
end = 11 * 30 + 30
dic = defaultdict(int)

for _ in range(N):
    a, b, c, d = map(int, input().split())

    if a >= 3 and b >= 1:
        a, b = 3, 1

    a *= 30
    c *= 30

    dic[a + b] = max(dic[a + b], c + d)

F.sort()
