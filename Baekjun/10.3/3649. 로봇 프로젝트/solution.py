while True:
    try:
        X = int(input()) * 10**7
        N = int(input())

        A = [int(input()) for _ in range(N)]
        A.sort()
        l, r = 0, N - 1
        flag = False
        while l < r:
            if A[l] + A[r] == X:
                print("yes", A[l], A[r])
                flag = True
                break
            elif A[l] + A[r] > X:
                r -= 1
            else:
                l += 1
        if not flag:
            print("danger")
    except:
        break
