from collections import deque
import sys

input = sys.stdin.readline

M, t, N = map(int, input().split())
a = []
for i in range(N):
    arrival, dest = input().split()
    a.append((int(arrival), int(dest == "left"), i))
a.sort()

time = 0
next = deque(a)
waiting = [deque(), deque()]
riding = deque()
loc = 1

res = [0] * N
while next or waiting[0] or waiting[1]:

    # 현재 방향 기준으로 기다리는 승객이 있는지 확인
    if waiting[loc]:
        pass
    elif waiting[loc ^ 1]:
        time += t
        loc ^= 1
    else:
        time = max(time, next[0][0])

    # 현재 시각까지 도착한 승객을 waiting 큐에 삽입
    while next and next[0][0] <= time:
        waiting[next[0][1]].append(next.popleft())

    # 현재 위치에 있는 승객들 중 태울 수 있는 손님들 태움
    while waiting[loc] and len(riding) < M:
        riding.append(waiting[loc].popleft())

    # 반대편으로 이동
    time += t
    loc ^= 1

    # 반대편에서 내림
    while riding:
        res[riding.popleft()[2]] = time

print("\n".join(map(str, res)))
