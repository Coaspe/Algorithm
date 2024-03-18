N, M = map(int, input().split())
cows = list(map(int, input().split()))
canes = list(map(int, input().split()))
eaten = [0] * M

for i in range(M):
    for j, c in enumerate(cows):
        if eaten[i] == canes[i]:
            break

        if c >= eaten[i]:
            a = min(c, canes[i]) - eaten[i]
            cows[j] += a
            eaten[i] += a


for c in cows:
    print(c)
