import sys

input = sys.stdin.readline

t = int(input())  # 테스트케이스 개수
for _ in range(t):
    n = int(input())  # 날의 수
    price = list(map(int, input().split()))  # 날 별 주가

    profit = 0  # 최대 이익

    max_price = price[-1]
    for i in range(n - 2, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += max_price - price[i]

    print(profit)
