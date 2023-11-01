N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = 0


def find():
    l, r = D - 1, D + 1
    while l != D:
        if A[l] or A[r]:
            break
        else:
            l -= 1
            r += 1
    return (l, r)


for _ in range(Q):
    I = list(map(int, input().split()))
    if I[0] == 1:
        A[I[1]] = not A[I[1]]
    elif I[0] == 2:
        D += I[1]
    else:
        pass
