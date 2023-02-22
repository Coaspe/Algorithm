# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-12015-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-%EA%B3%A8%EB%93%9C2-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89
import bisect
N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(1, N):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        dp[bisect.bisect_left(dp, arr[i])] = arr[i]
print(len(dp))
print(*dp)
