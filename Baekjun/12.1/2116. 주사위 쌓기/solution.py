from sys import stdin


def solution():
    input = stdin.readline

    N = int(input())
    dices = [list(map(int, input().split())) for _ in range(N)]

    M = [5, 3, 4, 1, 2, 0]

    def find_max(idx, die):
        max_val = 0
        for i in range(6):
            if i == idx or i == M[idx]:
                continue
            max_val = max(max_val, die[i])

        return max_val

    ans = 0

    for bottom in range(1, 7):
        ans_tmp = 0
        for die in dices:
            idx = die.index(bottom)
            ans_tmp += find_max(idx, die)
            bottom = die[M[idx]]
        ans = max(ans, ans_tmp)

    print(ans)


if __name__ == "__main__":
    solution()
