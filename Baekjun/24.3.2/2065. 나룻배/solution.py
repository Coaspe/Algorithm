from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
ints = lambda: map(int, input().split())

M, t, N = ints()
a = []
for i in range(N):
    arrival, dest = input().split()
    a.append((int(arrival), int(dest == "right"), i))
a.sort()

time = 0
next_passengers = deque(a)
waiting_passengers = [deque(), deque()]
riding_passengers = deque()
ship_location = 0

res = [0] * N
while next_passengers or waiting_passengers[0] or waiting_passengers[1]:
    if waiting_passengers[ship_location]:
        pass
    elif waiting_passengers[ship_location ^ 1]:
        time += t
        ship_location ^= 1
    else:
        time = max(time, next_passengers[0][0])

    while next_passengers and next_passengers[0][0] <= time:
        waiting_passengers[next_passengers[0][1]].append(next_passengers.popleft())

    while waiting_passengers[ship_location] and len(riding_passengers) < M:
        riding_passengers.append(waiting_passengers[ship_location].popleft())

    time += t
    ship_location ^= 1

    while riding_passengers:
        res[riding_passengers.popleft()[2]] = time

print("\n".join(map(str, res)))
