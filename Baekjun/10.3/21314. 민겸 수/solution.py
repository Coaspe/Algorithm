import sys

input = sys.stdin.readline

s = input().rstrip()

m = 0
max = ""
min = ""

for i in s:
    if i == "M":
        m += 1
    else:
        if m > 0:
            max += str(5 * (10**m))
            min += str(10**m + 5)
        else:
            max += "5"
            min += "5"
        m = 0

if m > 0:
    max += "1" * m
    min += str(10 ** (m - 1))

print(max)
print(min)
