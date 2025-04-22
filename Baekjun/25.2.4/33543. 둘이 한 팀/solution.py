from sys import stdin
from bisect import bisect_left

readLine = stdin.readline
readTwoInts = lambda: map(int, readLine().split())


def main():
    N = int(readLine())  # 능력치 개수

    sumBob = 0
    diffs = []
    for _ in range(N):
        a, b = readTwoInts()  # a = Alice_i, b = Bob_i
        sumBob += b  # Bob 능력치 합에 더함
        diffs.append(a - b)  # A_i - B_i 를 저장

    diffs.sort()

    prefixDiffs = [0] * (N + 1)
    for i in range(N):
        prefixDiffs[i + 1] = prefixDiffs[i] + diffs[i]

    delta = 0

    Q = int(readLine())  # 훈련(쿼리) 횟수
    for _ in range(Q):
        person, amountStr = readLine().split()
        amount = int(amountStr)

        if person == "A":
            delta -= amount
        else:
            delta += amount
            sumBob += amount * N

        idx = bisect_left(diffs, delta)

        result = sumBob + prefixDiffs[N] - prefixDiffs[idx] - (N - idx) * delta
        print(result)


if __name__ == "__main__":
    main()
