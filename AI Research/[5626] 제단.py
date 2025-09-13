N = int(input())
H = list(map(int, input().split()))

if H[0] > 0 or H[-1] > 0:
    print(0)
    exit()

H[0] = H[-1] = -1

row = [0] * (N // 2 + 1)
row[0] = 1

if any(h > N // 2 for h in H if h != -1):
    print(0)
    exit()

for i in range(1, N):
    a = H[i]
    nrow = [0] * (N // 2 + 1)
    if a == -1:
        for j in range(len(row)):
            nrow[j] = row[j - 1] * int(j > 0) + row[j]
            if j + 1 < len(row):
                nrow[j] += row[j + 1]
            nrow[j] %= 1000000007
    else:
        nrow[a] = row[a - 1] * int(a > 0) + row[a]
        if a + 1 < len(row):
            nrow[a] += row[a + 1]
        nrow[a] %= 1000000007

    row = nrow

print(row[0])
