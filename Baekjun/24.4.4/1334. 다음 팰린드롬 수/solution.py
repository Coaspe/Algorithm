def solution():
    N = int(input())

    if N <= 8:
        print(N + 1)
        return

    # 같은 자리수
    N_str = str(N)
    same = 0
    half = len(N_str) // 2

    if len(N_str) % 2:
        N_str = N_str[:half] + N_str[half] + N_str[:half][::-1]

        if int(N_str) > N:
            same = int(N_str)
        elif N_str[half] != "9":
            same = int(N_str[:half] + str(int(N_str[half]) + 1) + N_str[half + 1 :])
        elif N_str[half] == "9":
            tmp = N + 10 ** (half)
            tmp_str = str(tmp)

            if len(tmp_str) == len(N_str):
                same = int(tmp_str[:half] + tmp_str[half] + tmp_str[:half][::-1])

        if same:
            print(same)
            return
    else:
        N_str = N_str[:half] + N_str[:half][::-1]

        if int(N_str) > N:
            same = int(N_str)
        elif N_str[half] != "9":
            mid = str(int(N_str[half]) + 1)

            same = 2 * mid
            if half - 1 > 0:
                same = N_str[: half - 1] + same
            if half + 1 < len(N_str):
                same += N_str[half + 1 :]

            same = int(same)
        elif N_str[half] == "9":
            tmp = N + 10 ** (len(N_str) - half)
            tmp_str = str(tmp)
            if len(tmp_str) == len(N_str):
                same = int(tmp_str[:half] + tmp_str[:half][::-1])

        if same:
            print(same)
            return

    print(10 ** len(N_str) + 1)


if __name__ == "__main__":
    solution()
