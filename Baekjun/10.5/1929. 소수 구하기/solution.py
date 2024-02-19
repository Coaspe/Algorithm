M, N = map(int, input().split())

eratos = [0, 0] + [1] * (N - 1)


for i in range(2, N + 1):
    if i >= M and eratos[i]:
        print(i)
    for j in range(2 * i, N + 1, i):
        eratos[j] = 0
