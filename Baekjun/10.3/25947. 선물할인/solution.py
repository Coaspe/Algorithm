N, B, A = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
ans = 0
added = []
for s in S:
    if B >= s:
        B -= s
        added.append(s)
        ans += 1
    elif A:
        s2 = s // 2
        if B < s2:
            while A and B < s2 and added:
                B += added.pop() // 2
                A -= 1

            if A and B >= s2:
                B -= s2
                A -= 1
                ans += 1
        else:
            B -= s2
            ans += 1
            A -= 1
    else:
        break
print(ans)
