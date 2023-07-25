import math
D, P, Q = map(int, input().split())

smaller, larger = min(P, Q), max(P, Q)

l = 0
s = math.ceil(D / smaller)
gap = math.ceil(larger / smaller)

sub, ans = 10**9, 0

while True:
    cal = larger*l + smaller*s
    sub_tmp = cal - D
    print(l, s)
    if sub_tmp >= sub or sub_tmp < 0 or s < 0:
        print(ans)
        break

    sub = sub_tmp
    ans = cal
    l += 1
    s -= gap
