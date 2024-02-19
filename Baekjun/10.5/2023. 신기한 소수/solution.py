from math import sqrt, ceil


def solution():
    N = int(input())

    def dfs(n):
        if len(n) == N:
            print(n)
            return

        for i in range(1, 10, 2):
            new_n = int(n + str(i))
            flag = False

            for j in range(3, ceil(sqrt(new_n)) + 1, 2):
                if new_n % j == 0:
                    flag = True
                    break

            if not flag:
                dfs(str(new_n))

    for i in [2, 3, 5, 7]:
        dfs(f"{i}")


if __name__ == "__main__":
    solution()
