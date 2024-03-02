from heapq import heappop, heappush
from itertools import product


def solution(k, n, reqs):
    answer = 10**9
    all_permutations = product(range(1, n + 1), repeat=k)

    for kk in [perm for perm in all_permutations if sum(perm) == n]:
        qs = [[] for _ in range(k + 1)]

        tmp_answer = 0
        for request_time, period, case in reqs:
            while qs[case] and qs[case][0] <= request_time:
                heappop(qs[case])

            start = 0

            if len(qs[case]) == kk[case - 1]:
                start = heappop(qs[case])
                tmp_answer += start - request_time
                heappush(qs[case], start + period)
            else:
                heappush(qs[case], start + request_time + period)

        answer = min(answer, tmp_answer)

    return answer
