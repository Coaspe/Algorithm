import sys

input = sys.stdin.readline

s = list(input().strip())
s.sort()  # 정렬
n = len(s)
i, j = n // 2 - 1, n // 2 + int(n % 2)

ans = 0

while i > -1 and j < n:
    idx = j  # 팰린드롬이면 j와 바꿀 index
    if s[i] == s[j]:  # 팰린드롬인 부분이라면
        while s[i] == s[idx]:
            idx += 1  # idx 1씩 늘려가며 j와 바꿀 위치 찾기
            if idx == n:  # 없다면
                ans = -1  # 불가능
                break
        if ans == -1:
            break
    s[j], s[idx] = s[idx], s[j]  # swap
    i -= 1
    j += 1

if not ans:
    ans = "".join(s)

print(ans)
