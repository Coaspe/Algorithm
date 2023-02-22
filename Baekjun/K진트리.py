import sys
N, K, Q = map(int, input().split())

for _ in range(Q):
    a, b = map(int, input().split())
    ans = 0
    if K == 1:
        print(abs(a-b))
        continue
    while a != b:
        while a > b:
            ans += 1
            a = (a + K - 2) // K
        while b > a:
            ans += 1
            b = (b + K - 2) // K
    print(ans)

input = sys.stdin.readline
n, k, q = map(int, input().split())


for _ in range(q):
    a, b = map(int, input().split())
    answer = 0
    if k == 1:
        print(abs(a-b))
    else:
        while True:
            if a == b:
                print(answer)
                break
            if a > b:
                a = (a + k - 2) // k
                answer += 1
            else:
                b = (b + k - 2) // k
                answer += 1
