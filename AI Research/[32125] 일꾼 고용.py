for _ in range(int(input())):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    W = list(map(int, input().split()))

    cp = 0
    wp = 0

    m = {}
    m[0] = [0]

    for i in range(N):
        if C[i] == 1:
            cp += 1
            wp += W[i]
        else:
            cp -= 1
            wp -= W[i]

        m[cp] = m.get(cp, [])
        m[cp].append(wp)

    ans = 0

    for arr in m.values():
        arr.sort()
        l = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > K:
                l += 1
            ans += r - l

    print(ans)
