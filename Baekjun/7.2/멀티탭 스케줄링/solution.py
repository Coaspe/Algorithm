from collections import defaultdict
import bisect

N, K = map(int, input().split())
if N >= K:
    print(0)
    exit()

elec_list = list(map(int, input().split()))
dic = defaultdict(list)
plug = set()
cnt = 0

for idx, num in enumerate(elec_list):
    dic[num].append(idx)


def find_latest(idx):
    result = 0
    max_idx = -1
    for num in plug:
        i = bisect.bisect_left(dic[num], idx)

        if i == len(dic[num]):
            return num

        if dic[num][i] > max_idx:
            result = num
            max_idx = dic[num][i]

    return result


for idx, num in enumerate(elec_list):
    plug.add(num)
    if len(plug) > N:
        cnt += 1
        latest_used = find_latest(idx)
        plug.discard(latest_used)

print(cnt)
