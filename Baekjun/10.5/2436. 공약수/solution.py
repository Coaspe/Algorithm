# BOJ 2436. 공약수

import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solution():
    G, L = map(int, input().split())
    # num은 두 수의 곱
    num = L // G
    a = 1
    b = num
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0 and gcd(i, num // i) == 1 and a + b > i + num // i:
            a = i
            b = num // i
    print(a * G, b * G)


if __name__ == "__main__":
    solution()
