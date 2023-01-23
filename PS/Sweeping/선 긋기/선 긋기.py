import sys
input = sys.stdin.readline

N = int(input())

lines = [map(int, input().split()) for _ in range(N)]
lines.sort()

answer = 0
lo, hi = lines[0]
for a, b in lines:
    if a > hi:
        answer += (hi - lo)
        lo, hi = a, b
    hi = max(hi, b)
answer += (hi - lo)
print(answer)
