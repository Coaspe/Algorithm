N = int(input())
A = list(map(int, input().split()))
A.sort()

target = 1

for a in A:
    if target < a:
        break
    target += a

print(target)
# 1 3 5 2 6 4 7
# 1 2 3 5 6 4 7
# 1 2 3 4 5 6 7
