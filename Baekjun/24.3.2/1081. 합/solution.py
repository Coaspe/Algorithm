L, U = map(int, input().split())


def solve(page):
    ans = [0] * 10
    point = 1
    start = 1

    while start <= page:
        while page % 10 != 9 and start <= page:
            cal(page, ans, point)
            page -= 1

        if page < start:
            break

        while start % 10 != 0 and start <= page:
            cal(start, ans, point)
            start += 1

        start //= 10
        page //= 10

        for i in range(10):
            ans[i] += (page - start + 1) * point

        point *= 10

    return sum([i * ans[i] for i in range(10)])


def cal(x, ans, point):
    while x > 0:
        ans[x % 10] += point
        x //= 10


print(solve(U) - solve(max(L - 1, 0)))
