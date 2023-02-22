import sys


def find(planet):
    if parent[planet] == planet:
        return planet
    else:
        parent[planet] = find(parent[planet])
        return parent[planet]


def union(planet1, planet2):
    parent1 = find(planet1)
    parent2 = find(planet2)

    parent[parent2] = parent1


result = 0

N = int(sys.stdin.readline())
planet = []

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append([x, y, z, i])

edge = []
for x_y_z in range(3):
    # x, y, z 축 중 하나로 정렬
    planet.sort(key=lambda v: v[x_y_z])
    # 인덱스
    before = planet[0][3]
    for i in range(1, N):
        # 인덱스
        cur = planet[i][3]
        edge.append(
            [before, cur, abs(planet[i][x_y_z] - planet[i - 1][x_y_z])])
        before = cur
edge.sort(key=lambda v: v[2])

parent = [i for i in range(N)]
for planet1, planet2, distance in edge:
    if find(planet1) != find(planet2):
        result += distance
        union(planet1, planet2)

print(result)
