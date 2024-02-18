N, M = map(int, input().split())
cake = list(map(int, input().split()))

ten_cake = []
other_cake = []

cake.sort()

for c in cake:
    if c % 10 == 0:
        ten_cake.append(c)
    else:
        other_cake.append(c)

count = M
result = 0
for t in ten_cake:
    if count <= 0:
        break

    count -= t // 10 - 1
    result += t // 10

if count < 0:
    result -= -1 * count + 1
else:
    for o in other_cake:
        if count <= 0:
            break
        count -= o // 10
        result += o // 10

    if count < 0:
        result -= -1 * count

print(result)
