def calculate_ans(N: int, I: list[int], A: list[int]) -> int:
    ans = 0
    T = sorted(zip(I, A), key=lambda x: x[1])

    for idx in range(N):
        i, a = T[idx]
        ans += a * idx + i

    return ans


if __name__ == "__main__":
    N = int(input())
    I = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ans = calculate_ans(N, I, A)
    print(ans)
