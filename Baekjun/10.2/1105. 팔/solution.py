L, R = input().split()

if len(L) != len(R):
    print(0)
    exit(0)

ans = 0
for i in range(len(L)):
    if L[i] == R[i] == "8":
        ans += 1
    elif L[i] != R[i]:
        break

print(ans)
