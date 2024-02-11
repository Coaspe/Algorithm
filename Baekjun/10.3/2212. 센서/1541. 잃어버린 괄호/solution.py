SS = input().split("-")
ans = 0

if SS[0] != "":
    ans += sum(map(int, SS[0].split("+")))

for i in range(1, len(SS)):
    ans += sum(map(int, SS[i].split("+"))) * -1

print(ans)
