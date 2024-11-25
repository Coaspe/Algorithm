from collections import deque

N, M, K = map(int, input().split())

if N > M * K or N - K < M - 1:
    print(-1)
    exit(0)

remaining_elements = deque(range(K + 1, N + 1))
result = list(range(K, 0, -1))

if M - 1 == 0:
    print(" ".join(map(str, result)))
    exit(0)

group_size, extra_elements = divmod(N - K, M - 1)

while remaining_elements:
    current_group = []
    for _ in range(group_size):
        current_group.append(remaining_elements.popleft())
    if extra_elements > 0:
        current_group.append(remaining_elements.popleft())
        extra_elements -= 1
    result.extend(current_group[::-1])

print(" ".join(map(str, result)))
