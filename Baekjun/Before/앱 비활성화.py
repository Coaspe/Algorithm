def solution():
    N, M = map(int, input().split())
    # 활성화 되어 있는 앱의 바이트 수
    A = list(map(int, input().split()))
    # 비활성화 했을 경우의 비용
    C = list(map(int, input().split()))
    MAX = 100 * 100 + 1

    # 비활성화 비용으로 총 i만큼 사용했을 때, 확보한 최대 바이트 수
    dp = [-1] * (MAX)
    dp[0] = 0

    for i in range(N):
        for j in range(MAX - 1, -1, -1):
            if dp[j] != -1 and j + C[i] < MAX:
                dp[j + C[i]] = max(dp[j + C[i]], dp[j] + A[i])

    for i in range(MAX):
        if dp[i] >= M:
            print(i)
            break


if __name__ == "__main__":
    solution()
