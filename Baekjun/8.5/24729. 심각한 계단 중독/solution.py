import sys

input = sys.stdin.readline

n = int(input())
M = list(map(int, input().split()))

L = [0] * 100002
for k in M:
    L[k] += 1

# 가장 작은 수에서 시작
start = min(M)
now = start

# 가장 작은 수에서 시작해서 값의 +1, -1이 있는지 확인하며 값을 갱신한다.
while True:
    L[now] -= 1
    if L[now + 1]:
        now += 1
    elif L[now - 1]:
        now -= 1
    else:
        break

ans = 1
# 값이 남아있으면 안 된다.
for i in range(100001):
    if L[i]:
        ans = -1
        break

# 시작과 끝의 차이는 1이 되어야 한다.
if now - start != 1:
    ans = -1

print(ans)
