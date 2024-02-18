def func(idx, A):
    for i in range(6):
        if A[idx][0] == 0:
            break

        if idx == i:
            continue

        if A[idx][0] >= A[i][2]:
            A[idx][0] -= A[i][2]
            A[i][2] = 0
        else:
            A[i][2] -= A[idx][0]
            A[idx][0] = 0

    return A[idx][0]


def solution():
    ans = []
    for _ in range(4):
        AA = list(map(int, input().split()))
        A = [AA[i : i + 3] for i in range(0, 16, 3)]
        print(A)
        draw = 0

        for idx, a in enumerate(A):
            print(a)
            # 승 = i-2, 무 = i-1, 패 = i
            if sum(a) != 5:
                ans.append(0)
                break

            draw = abs(draw - a[1])

            if func(idx, A):
                break

        if len(ans) == _ + 1:
            continue

        for a, _, b in A:
            if a != 0 or b != 0:
                ans.append(0)
                break

        if len(ans) != _ + 1:
            ans.append(1)

    print(*ans)


if __name__ == "__main__":
    solution()
