'''
문제
0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

1 ≤ i < j ≤ M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 만약 연산을 K번 할 수 없으면 -1을 출력한다.
'''

import collections
N, K = map(int, input().split())
M = len(str(N))
q = collections.deque([(N, K)])
visited = set([(N, K)])
answer = 0

while q:
    n, k = q.pop()
    if k == 0:
        answer = max(answer, n)
        continue
    n = list(str(n))
    for i in range(M-1):
        for j in range(i+1, M):
            if i == 0 and n[j] == '0':
                continue
            n[i], n[j] = n[j], n[i]
            nn = int(''.join(n))
            n[i], n[j] = n[j], n[i]
            if (nn, k-1) not in visited:
                q.append((nn, k-1))
                visited.add((nn, k-1))
print(answer if answer else -1)
