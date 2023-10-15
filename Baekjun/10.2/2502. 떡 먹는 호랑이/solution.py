D, K = map(int, input().split())


def check(l, r):
    TD = D - 3
    x = [r, l]

    while TD:
        TD -= 1

        nr = r - l

        if nr > l or nr < 1:
            return False

        r, l = l, nr
        x.append(nr)

    return (l, r)


t1 = K // 2
t2 = K - t1

while t1 >= 1:
    result = check(t1, t2)
    if result:
        print(result[0])
        print(result[1])
        break
    else:
        t1 -= 1
        t2 += 1
