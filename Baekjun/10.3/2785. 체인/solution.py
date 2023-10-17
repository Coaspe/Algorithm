N = int(input())
A = list(map(int, input().split()))

A.sort()


def sol(N):
    count = 0
    use_chain = 0
    for chain in A:
        if chain >= N - 1:
            return use_chain + N - 1
        else:
            N -= chain + 1
            use_chain += chain

    return count


print(sol(N))
