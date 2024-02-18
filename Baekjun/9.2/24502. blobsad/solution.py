"""
c 라는 값을 계속 K 로 나눈 나머지를 관리한다.
이전까지 블롭들의 합이 c에 저장되어 있고 이게 K / 2 이하라면 중앙값이 더 오른쪽에 있다는 것이므로 c 를 정답에 더해주고
그렇지 않으면 왼쪽으로 올 것들의 개수 K - c 를 더해준다.
이렇게 더해주는 이유는 한칸 한칸을 움직이는데 필요한 비용을 계산하기 때문이다. 
어떤 블롭이 2칸 이상을 이동한다고 생각해보자.
그럼 총 정답에 그 거리의 합 모두가 더해져야 하는데, 더 움직여야 할 블롭들의 개수들이 각 칸마다 정답에 더해지는 것은 옳다.
"""

N, K = map(int, input().split())
l = list(map(int, input().split()))
c = l[0] % K
ans = 0

for i in range(1, N):
    if K // 2 >= c:
        ans += c
        print("1", c)
    else:
        ans += K - c
        print("2", c)

    # ans += c if c <= K // 2 else K - c
    c = (c + l[i]) % K

if c:
    print("blobsad")
else:
    print(ans)
