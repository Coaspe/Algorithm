N = int(input())


acc, n = 3, 0


def moo(acc, cur, n):
    prev = (acc - cur) // 2

    if n <= prev:
        return moo(prev, cur - 1, n)
    elif n > prev + cur:
        return moo(prev, cur - 1, n - prev - cur)
    else:
        return "o" if n - prev - 1 else "m"


while N > acc:
    n += 1
    acc = 2 * acc + n

print(moo(acc, n + 3, N))
