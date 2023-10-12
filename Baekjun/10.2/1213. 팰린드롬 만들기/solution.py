from collections import Counter

S = input()

CS = Counter(S)

odd = -1
for i in CS:
    if CS[i] % 2:
        if odd != -1:
            print("I'm Sorry Hansoo")
            exit(0)
        else:
            odd = i

LS = sorted(CS.keys(), reverse=True)

ans = ""
if odd != -1:
    ans += odd
    CS[odd] -= 1


for alpha in LS:
    ans = alpha * (CS[alpha] // 2) + ans + alpha * (CS[alpha] // 2)

print(ans)
