import sys


def merge_sort(start, end):
    global swap_cnt, ARR

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        front_idx, back_idx = start, mid + 1
        new_arr = []

        while front_idx <= mid and back_idx <= end:
            if ARR[front_idx] <= ARR[back_idx]:
                new_arr.append(ARR[front_idx])
                front_idx += 1
            else:
                new_arr.append(ARR[back_idx])
                back_idx += 1
                swap_cnt += mid - front_idx + 1

        if front_idx <= mid:
            new_arr = new_arr + ARR[front_idx: mid + 1]
        if back_idx <= end:
            new_arr = new_arr + ARR[back_idx: end + 1]

        for i in range(len(new_arr)):
            ARR[start + i] = new_arr[i]


if __name__ == "__main__":
    swap_cnt = 0
    N = int(sys.stdin.readline())
    ARR = list(map(int, sys.stdin.readline().split()))
    merge_sort(0, N - 1)
    print(swap_cnt)
