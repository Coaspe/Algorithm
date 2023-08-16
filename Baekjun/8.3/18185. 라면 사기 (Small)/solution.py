N = int(input())
factory = list(map(int, input().split()))
factory.append(0)
factory.append(0)

ans = 0

for i in range(N):
    if factory[i + 1] > factory[i + 2]:
        c5 = min(factory[i], factory[i + 1] - factory[i + 2])
        factory[i] -= c5
        factory[i + 1] -= c5
        ans += c5 * 5

        c7 = min(factory[i], factory[i + 1], factory[i + 2])
        factory[i] -= c7
        factory[i + 1] -= c7
        factory[i + 2] -= c7
        ans += c7 * 7
    else:
        c7 = min(factory[i], factory[i + 1])
        factory[i] -= c7
        factory[i + 1] -= c7
        factory[i + 2] -= c7
        ans += c7 * 7

        c5 = min(factory[i], factory[i + 1])
        factory[i] -= c5
        factory[i + 1] -= c5
        ans += c5 * 5

    ans += factory[i] * 3

print(ans)
