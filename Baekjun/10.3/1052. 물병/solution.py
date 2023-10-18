import sys

input = sys.stdin.readline().rstrip

n, k = map(int, input().split())

answer = 0

while n.bit_count() > k:
    val = n & -n
    answer += val
    n += val

print(answer)
