from itertools import permutations


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for p in permutations(A, N):
        prev = 0
        candid = {0}
        tmp_ans = 0
        for n in p:
            prev += n
            if prev - 50 in candid:
                tmp_ans += 1
                candid.remove(prev - 50)
            else:
                candid.add(prev)

        ans = max(ans, tmp_ans)
    print(ans)


if __name__ == "__main__":
    solution()
