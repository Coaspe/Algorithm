'''
문제
황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다.
이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.

하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.

우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.

또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.

이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

입력
첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.

두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

출력
첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.
'''
import math
import sys
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')


def prim(start):
    distances[start] = 0  # 시작 정점의 거리를 0으로 설정
    res = 0.0

    # N번 반복한다.
    for _ in range(N):
        minNextNode, minDist = 0, INF

        # 현재 연결된 집합에서 아직 방문하지 않았고 거리가 가까운 좌표를 찾는다.
        for i in range(1, N+1):
            if not visited[i] and distances[i] < minDist:
                minNextNode = i
                minDist = distances[i]

        # 위에서 찾은 좌표를 방문 체크해주고 거리를 res에 더해준다.
        visited[minNextNode] = True
        res += minDist

        # 새롭게 추가된 좌표에서 연결되지 않은 좌표 중 갈 수 있는 좌표와 더 작은 거리 값을 가지고 있는 좌표를 찾아서
        # distances 배열을 갱신해준다.
        for dist, node in graph[minNextNode]:
            if not visited[node] and distances[node] > dist:
                distances[node] = dist

    return '{:.2f}'.format(res)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = defaultdict(list)
    coords = [(0, 0)]  # 좌표 리스트
    visited = [False] * (N + 2)  # 집합에 포함된 좌표인지를 체크하기 위한 리스트
    distances = [INF for _ in range(N + 1)]  # 현재 집합에서 갈 수 있는 좌표들의 최소 거리

    for _ in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))

    # 이미 연결된 통로 입력
    # 거리를 0으로 설정하여 넣어준다. 0보다 작은 거리 값은 없기 때문에 MST를 구성할 때 해당 경로가 선택됨이 보장된다.
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((0, b))
        graph[b].append((0, a))

    for i in range(1, N + 1):
        for j in range(i+1, N + 1):
            x = abs(coords[j][0] - coords[i][0])
            y = abs(coords[j][1] - coords[i][1])
            dist = math.sqrt(x ** 2 + y ** 2)

            graph[i].append((dist, j))
            graph[j].append((dist, i))

    # 시작 정점은 임의로 1로 설정하여 프림 알고리즘 수행
    print(prim(1))
