# 162
# 81
# 8
# 4
# 2

A, B = map(int, input().split())
ans = 1
while A != B:
    BB = str(B)
    if B == 1:
        print(-1)
        exit(0)
    if B % 2 == 0:
        B //= 2
    elif BB[-1] == "1" and B != 1:
        B = int(BB[:-1])
    else:
        print(-1)
        exit(0)
    ans += 1
print(ans)
