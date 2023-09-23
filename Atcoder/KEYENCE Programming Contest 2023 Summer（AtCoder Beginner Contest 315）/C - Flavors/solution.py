N = int(input())
val = [[0, 0] for _ in range(N + 1)]

for _ in range(N):
    f, s = map(int, input().split())

    if s == val[f][1]:
        val[f][0] = s
    elif s > val[f][1]:
        val[f] = [val[f][1], s]
    elif val[f][0] < s < val[f][1]:
        val[f][0] = s
max_idx = 0

for idx, (f, s) in enumerate(val):
    if s > val[max_idx][1]:
        max_idx = idx

same = int(val[max_idx][0] / 2) + val[max_idx][1]

diff = val[max_idx][1]

max_idx2 = 0

for i in range(1, N + 1):
    if i == max_idx:
        continue

    max_idx2 = max(max_idx2, i, key=lambda x: val[x][1])

diff += val[max_idx2][1]

print(max(same, diff))
