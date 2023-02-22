from sys import stdin

input = stdin.readline
T = int(input())


def solve():
    F = int(input())
    for _ in range(F):
        a, b = input().split()
        p_a = find(a)
        p_b = find(b)
        if p_a != p_b:
            union(p_a, p_b)

        print(friends[p_a])


def find(a):
    if a in friends:
        if type(friends[a]) == str:
            friends[a] = find(friends[a])
            return friends[a]
    else:
        friends[a] = 1
    return a


def union(a, b):
    friends[a] += friends[b]
    friends[b] = a


for _ in range(T):
    friends = {}
    solve()
