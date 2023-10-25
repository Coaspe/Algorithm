# input
N = int(input())
SIZE = 1000001
player = list(map(int, input().split()))
MAX = 0
card = [False] * SIZE
score = [0] * SIZE

for i in player:
    MAX = max(MAX, i)
    card[i] = True

# solution
for i in player:
    for j in range(i * 2, MAX + 1, i):
        if card[j]:
            score[i] += 1
            score[j] -= 1

# output
print(" ".join(map(str, [score[num] for num in player])))
