str = input()

d = l = r = 0

for i in range(len(str)):
    if str[i] == "(":
        l += 1
        d += 1
    else:
        r += 1
        d -= 1
        if d < 0:
            print(r)
            exit(0)

    if d == 1:
        l = 0
print(l)
