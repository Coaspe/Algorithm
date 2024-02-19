S = input()
all_same = len(S) == 1

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        all_same = False
        break
    else:
        all_same = True

if all_same:
    print(-1)
    exit(0)

N = 0
is_palindrome = True

while N < len(S) // 2:
    if S[N] == S[-(N + 1)]:
        N += 1
    else:
        is_palindrome = False
        break

if is_palindrome:
    print(len(S) - 1)
else:
    print(len(S))
