N, X = map(int, input().split())

ans = ["A"] * N

if X < N or X > 26 * N:
    print("!")
else:
    X -= N
    i = N - 1
    while X > 0:
        if X >= 25:
            ans[i] = "Z"
            X -= 25
        else:
            ans[i] = chr(ord("A") + X)
            X = 0
        i -= 1
    print("".join(ans))
