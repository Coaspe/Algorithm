import sys

input = sys.stdin.readline


length, width, height = map(int, input().split())
total = length * width * height
N = int(input())
cube = [tuple(map(int, input().split())) for _ in range(N)]
cube.sort(reverse=True)

answer, total_now = 0, 0
for c_idx, c_cnt in cube:
    # 다음 순서 = 이전 정육면체 부피의 1/8이므로 이전까지의 개수에 8을 곱해줌 (예 : 4*4*4 1개 = 2*2*2 8개)
    total_now *= 8

    c_len = 2**c_idx

    cnt_limit = (length // c_len) * (width // c_len) * (
        height // c_len
    ) - total_now  # 현재 공간에 채울 수 있는 개수 - 지금까지 채운 개수
    cnt_limit = min(c_cnt, cnt_limit)  # 실제로 채우기 가능한 개수

    answer += cnt_limit
    total_now += cnt_limit

if total_now == total:
    print(answer)
else:
    print(-1)
