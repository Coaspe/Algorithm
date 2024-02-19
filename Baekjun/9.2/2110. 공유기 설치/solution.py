N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
e, s = (house[-1] - house[0]), 1


while s + 1 < e:
    mid = (s + e) // 2

    cnt = 1

    prev_house = house[0]

    for i in range(1, N):
        if house[i] - prev_house >= mid:
            cnt += 1
            prev_house = house[i]

    if cnt >= C:
        s = mid
    else:
        e = mid


print(s if C != 2 else house[-1] - house[0])
