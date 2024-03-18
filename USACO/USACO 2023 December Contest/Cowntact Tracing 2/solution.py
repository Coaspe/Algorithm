import math

N = int(input())
cows = "0" + input() + "0"

minday = N + 1
ylist = []

# 시퀀스가 가장 느리게 끝날 수 있는 시간들을 모아서 최소값을 찾는다.
for i in range(1, N + 1):
    if cows[i - 1] == "0" and cows[i] == "1":
        bjt = i
    if cows[i] == "1" and cows[i + 1] == "0":
        ylist.append(i - bjt + 1)
        if bjt == 1 or i == N:
            # 끝이 처음이나 마지막이면 하루에 1개씩
            day = i - bjt
        else:
            day = (i - bjt) // 2
        minday = min(minday, day)

ans = 0
for i in ylist:
    ans += math.ceil(i / (1 + 2 * minday))
print(ans)
