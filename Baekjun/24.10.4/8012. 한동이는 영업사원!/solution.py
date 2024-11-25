def count_operations(sequence):
    N = len(sequence)
    if N <= 1:
        return 0

    # 각 수를 2의 거듭제곱으로 나눈 나머지와 필요한 연산 횟수를 계산
    def get_power_and_ops(num):
        odd_part = num
        operations = 0
        while odd_part % 2 == 0:
            odd_part //= 2
            operations -= 1
        return odd_part, operations

    # 수열을 오름차순으로 만들기 위해 필요한 최소 연산 횟수 계산
    def min_operations_to_sort():
        # 각 수의 홀수 부분과 현재까지의 연산 횟수 계산
        numbers = []
        for x in sequence:
            odd, ops = get_power_and_ops(x)
            numbers.append((odd, ops))

        operations_needed = 0
        for i in range(N - 1):
            if numbers[i][0] > numbers[i + 1][0]:
                # 왼쪽 수가 더 큰 경우, 오른쪽 수를 키워야 함
                diff = (numbers[i][0] - numbers[i + 1][0]).bit_length()
                operations_needed += diff
                numbers[i + 1] = (
                    numbers[i + 1][0] * (1 << diff),
                    numbers[i + 1][1] + diff,
                )
            elif (
                numbers[i][0] == numbers[i + 1][0] and numbers[i][1] > numbers[i + 1][1]
            ):
                # 홀수 부분이 같은 경우, 연산 횟수를 맞춰줌
                operations_needed += numbers[i][1] - numbers[i + 1][1]
                numbers[i + 1] = (numbers[i + 1][0], numbers[i][1])

        return max(0, operations_needed)

    return min_operations_to_sort()


def solve_queries(N, Q, A, queries):
    results = []
    for l, r in queries:
        # 인덱스를 0-based로 변환
        subsequence = A[l - 1 : r]
        result = count_operations(subsequence)
        results.append(result)
    return results


# 입력 처리
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for _ in range(Q):
    l, r = map(int, input().split())
    queries.append((l, r))

# 결과 출력
results = solve_queries(N, Q, A, queries)
for result in results:
    print(result)
