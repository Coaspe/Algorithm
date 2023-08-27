N, M = map(int, input().split())
cards = list(range(1, N + 1))

for _ in range(M):
    x, y = map(int, input().split())
    cards[x - 1] += 1
    cards[y - 1] -= 1

cards_set = set(cards)

if len(cards_set) != N:
    print(-1)
    exit()

for i in cards_set:
    if i > N or i < 1:
        print(-1)
        exit()

print(*cards)
