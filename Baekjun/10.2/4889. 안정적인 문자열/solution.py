T = 0
while True:
    T += 1
    S = list(input())

    if S[0] == "-":
        break

    a = b = ans = 0

    while S:
        s = S.pop()
        if s == "{":
            if b == 0:
                a += 1
            else:
                b -= 1
        else:
            b += 1

    if a % 2:
        ans = 2 + (a - 1) // 2 + (b - 1) // 2
    else:
        ans = a // 2 + b // 2

    print(f"{T}. {ans}")
