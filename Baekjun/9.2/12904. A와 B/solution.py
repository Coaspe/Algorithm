S, T = input(), input()

while len(S) != len(T):
    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

print(1 if S == T else 0)
