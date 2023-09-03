S = input()

nol = 0
satu = 0

for i in S:
    if i == "0":
        nol += 1
    else:
        satu += 1

if nol > satu:
    print(len(S) * "1")
elif satu > nol:
    print(len(S) * "0")
else:
    print(chr(ord("0") + ord("1") - ord(S[0])) + S[0] * (len(S) - 1))
# 4 3 2 1
