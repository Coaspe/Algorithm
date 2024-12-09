def is_possible(max_dist, n, k, dat):
    min_y = dat[0][1]
    max_y = dat[0][1]
    cnt = 1

    for i in range(1, n):
        if max(abs(min_y - dat[i][1]) / 2, abs(max_y - dat[i][1]) / 2) <= max_dist:
            min_y = min(min_y, dat[i][1])
            max_y = max(max_y, dat[i][1])
        else:
            min_y = dat[i][1]
            max_y = dat[i][1]
            cnt += 1

    return cnt <= k


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())
    idx = 1

    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        idx += 2
        tt = list(map(float, input().split()))
        dat = [(tt[i], tt[i + 1]) for i in range(0, n * 2, 2)]
        dat.sort()

        lo, hi = -1, 1e9 + 1
        while hi - lo > 0.1:
            mid = (lo + hi) / 2
            if is_possible(mid, n, k, dat):
                hi = mid
            else:
                lo = mid

        results.append(f"{lo:.1f}")

    print("\n".join(results))


if __name__ == "__main__":
    main()
