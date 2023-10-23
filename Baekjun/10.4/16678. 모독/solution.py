N = int(input())
honors = [int(input()) for _ in range(N)]

max_honor = 1
action = 0

for num in sorted(honors):
    if num >= max_honor:
        action += num - max_honor
        max_honor += 1

print(action)
