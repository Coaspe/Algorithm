from bisect import bisect_left

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
N += 1

prefix = []
ans = N + 1

for a in A:
    if a == S:
        print(1)
        exit(0)

    if not prefix:
        prefix.append(a)
    else:
        prefix.append(prefix[-1] + a)

for i in range(1, N):
    P = prefix[i]
    idx = bisect_left(prefix, P - S)

    if prefix[idx] > P - S:
        idx -= 1

    if idx >= 0 and prefix[idx] <= P - S:
        while idx < N and idx < i:
            if A[idx + 1] != 0:
                break
            idx += 1

        ans = min(ans, i - idx)

        if ans == 1:
            break

print(ans if ans != N + 1 else 0)
