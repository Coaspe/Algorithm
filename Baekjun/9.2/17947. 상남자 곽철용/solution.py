import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

card = [1] * (4 * N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    card[a] = 0
    card[b] = 0


chulyong = list(map(int, input().split()))
card[chulyong[0]] = 0
card[chulyong[1]] = 0

chulyong_score = abs(chulyong[0] % K - chulyong[1] % K)

card = [i for i in range(1, 4 * N + 1) if card[i]]

for i in range(len(card)):
    card[i] %= K

card.sort()

left = right = answer = 0

while right < len(card) and answer < M - 1:
    if card[right] - card[left] > chulyong_score:
        answer += 1
        right += 1
        left += 1
    else:
        right += 1

print(answer)
