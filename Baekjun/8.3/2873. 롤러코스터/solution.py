R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]

# 홀수이면 지그재그
# R, C 모두 짝수이면 (R-2, C), (R-1, C-2) 중에 뭐가 더 큰지 비교
ans = ""
if R % 2:
    for i in range(R):
        ans += ("L" if i % 2 else "R") * (C - 1)
        if i != R - 1:
            ans += "D"
elif C % 2:
    for i in range(C):
        ans += ("U" if i % 2 else "D") * (R - 1)
        if i != C - 1:
            ans += "R"
else:
    if B[R - 2][C - 1] > B[R - 1][C - 2]:
        for i in range(R - 2):
            ans += ("L" if i % 2 else "R") * (C - 1)
            ans += "D"

        for i in range(C - 2):
            ans += "U" if i % 2 else "D"
            ans += "R"

        ans += "RD"
    else:
        for i in range(C - 2):
            ans += ("U" if i % 2 else "D") * (R - 1)
            ans += "R"

        for i in range(R - 2):
            ans += "L" if i % 2 else "R"
            ans += "D"

        ans += "DR"

print(ans)
