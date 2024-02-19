# BOJ 1011. Fly me to the Alpha Centauri

import sys
from math import sqrt, ceil


def solution():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        dist = y - x

        square = ceil(sqrt(dist)) ** 2
        mid = square - ceil(sqrt(square))

        if dist <= mid:
            print(2 * ceil(sqrt(square)) - 2)
        else:
            print(2 * ceil(sqrt(square)) - 1)


if __name__ == "__main__":
    solution()
