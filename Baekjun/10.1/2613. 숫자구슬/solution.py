import sys

input = sys.stdin.readline


def is_possible(target):
    grpCnt = 1
    total = 0
    for number in numbers:
        total += number
        if total > target:
            grpCnt += 1
            total = number

    return grpCnt <= M


def solve(target):
    count = 0
    total = 0
    result = []
    m = M
    for idx in range(N):
        total += numbers[idx]
        if total > target:
            m -= 1
            total = numbers[idx]
            result.append(count)
            count = 0
        count += 1
        if N - idx == m:
            break

    while m:
        result.append(count)
        count = 1
        m -= 1
    return result


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left = max(numbers)
right = sum(numbers)

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
print(*solve(left))
