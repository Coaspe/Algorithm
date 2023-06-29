import math
T = int(input())


def solution():
    N = int(input())
    final = list(map(int, input().split()))
    max_val = -math.inf
    for f in final:
        if f < 0:
            print(f)
            return
        else:
            max_val = max(max_val, f)
    print(max_val)


while T:
    T -= 1
    solution()
