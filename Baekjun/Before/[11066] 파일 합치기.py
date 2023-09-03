import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    d = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2, n):
            d[i][j] = d[i][j-1] + f[j]

    for v in range(2, n):
        for i in range(n-v):
            d[i][i+v] += min([d[i][k] + d[k+1][i+v] for k in range(i, i+v)])

    print(d[0][n-1])

input = sys.stdin.readline


def solve():
    N, A = int(input()), [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(2, N+1):  # 부분 파일의 길이(몇개 합쳤냐? 두개합친거에서 3개를 구하고 4개를 구하고.(결국 앞에더할까 뒤에더할까))
        for j in range(1, N+2-i):   # 시작점
            # 원래 행별 계산이면 j가 앞쪽 인자로만 들어가나 대각선이기때문에 행, 열 모두에 들어가 1씩 증가시켜준다.
            # DP[1][3] -> min(DP[1][2]+DP[3][3],DP[1][1] + DP[2][3]) + S[3]-S[1](이게 범위 합에 누적합을 더하는 방식.)
            # 플로이드 워셜처럼 k를 끼고 최솟값이 있냐 없냐? 어느경로로 가는게 좋냐 최솟값 택해서 누적합 더해주기.
            # k는 결국 길이 범위인 i보다 작은 범위 즉 길이가 i면 부분 길이 k는 0부터 i-1까지.
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1]
                               for k in range(i-1)]) + (S[j+i-1] - S[j-1])

    print(DP[1][N])


for _ in range(int(input())):
    solve()
