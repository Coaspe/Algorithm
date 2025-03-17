from bisect import bisect_left


def solution(cookie):
    answer = 0
    N = len(cookie)
    pf = [0]

    for c in cookie:
        pf.append(pf[-1] + c)

    for m in range(1, N + 1):
        for l in range(m + 1):
            sub = pf[l - 1]

            ans = pf[m] - sub
            serach = 2 * ans + sub

            idx = bisect_left(pf, serach, lo=m + 1)

            if m + 1 <= idx <= N and pf[idx] == serach:
                answer = max(answer, ans)

    return answer
