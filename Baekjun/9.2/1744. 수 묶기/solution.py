N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
ans = 0
vals = []

while arr:
    x = arr.pop()

    if x > 0:
        arr.append(x)
        break

    if vals:
        ans += vals[0] * x
        vals = []
    else:
        vals.append(x)

ans += sum(vals)

vals = -1
arr.reverse()

ans += sum(arr)

while arr:
    x = arr.pop()

    if vals > 0:
        if vals * x > vals + x:
            ans = ans - vals - x + vals * x
        vals = -1
    else:
        vals = x

print(ans)
