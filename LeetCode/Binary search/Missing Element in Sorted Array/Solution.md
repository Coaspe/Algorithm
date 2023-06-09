# Approach 2: Binary Search

## Intuition

>Missing number의 수가 k 보다 작거나 같아질 때의 가장 왼쪽 요소를 찾는 것이 아이디어입니다.

![Alt text](https://leetcode.com/problems/missing-element-in-sorted-array/solutions/310531/Figures/1060/inary.png)

## Algorithm

- 인덱스 `idx`까지 몇개의 missing number가 있는지 반환하는 `missing(idx)`를 구현합니다. 함수는 `num[idx] - nums[0] - idx`를 반환합니다.
- `missing(idx - 1) < k <= missing(idx)`인 인덱스를 _binary search_ 로 탐색합니다.
- k번째로 작은 `nums[idx - 1] + k - missing(idx - 1)`를 반환합니다.