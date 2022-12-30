# Solution

## OverView

### DP 문제라는 것을 알아차리기

이 문제가 DP라는 단서가 두가지 있습니다.

첫 번째, 문제에서 무언가를 하는 **"방법의 수"** 를 묻습니다.

두 번째, 이전에 내린 결정에 **의존할 수 있는 결정**을 내려야 합니다. 이 문제에서, 우리는 주어진 포스트를 어떤 색으로 칠해야 하는지 결정해야 하는데, 이것은 이전의 결정에 따라 달라질 수 있습니다. 예를 들어, 첫 번째, 두 번째 포스트를 같은 색으로 칠하면 세 번째 포스트는 같은 색으로 칠할 수 없습니다.

이 두개는 DP 문제의 특징입니다.

### DP 문제를 해결하는 방법

DP 문제는 보통 3개의 컴포넌트로 구성됩니다. **대부분의 DP 문제는 이 방법으로 해결이 가능하므로** 이 컴포넌트들을 배우는 것은 매우 중요합니다.

첫째, 주어진 상태에 대한 문제의 답을 나타내는 함수나 배열이 필요합니다. 이 문제에서, `totalWays`라는 함수가 있다고 가정합시다. `totalWays(i)`는 `i`개의 포스트를 칠하는 방법의 수를 반환합니다. 하나의 인자만을 가지고 있기 때문에, 이 문제는 1차원 DP 문제입니다.

둘째, `totalWays(3)` 그리고 `totalWays(4)` 같은 상태 간의 전환 방법이 필요합니다. 이것을 **recurrence relation**이라 부르고 이것을 해결하는 것이 DP 문제를 풀 때 가장 어려운 부분입니다. Recurrence relation에 대해서는 밑에서 이야기합시다.

세번째는 베이스 케이스를 만드는 것입니다. 하나의 포스트가 있을 때, `k`개의 방법이 존재합니다. 두개의 포스트가 있다면 `k * k`개의 방법이 존재합니다. 그러므로 `totalWays(1) = k, totalWays(2) = k * k` 입니다.

### Recurrence Relation 찾기

우리는 `totalWays(1)`, `totalWays(2)`를 알고 있고 이제 `3 <= i <= n` 에서 `totalWays(i)`의 공식을 도출해야합니다. $i^{th}$ 포스트를 칠하는 데 얼마나 많은 방법이 있을지 생각해봅시다. 두가지 옵션이 존재합니다:

1. 이전 포스트와 다른 색을 사용합니다. 다른 색을 사용하면, `k-1`개의 색이 존재합니다. 이것은 $(i-1)^{th}$ 포스트와 다른 색으로 $i^{th}$ 포스트를 칠하는 방법이 `(k - 1) * totalWays(i - 1)`개 존재한다는 의미입니다.

2. 이전 포스트와 같은 색을 사용합니다. $(i-1)^{th}$ 포스트와 같은 색으로 $i^{th}$를 칠하는 방법은 1가지 뿐임으로 `1 * totalWays(i - 1)`개가 존재합니다. 그러나, 이 문제는 세 개의 연속된 포스트를 같은 색으로 칠할 수 없다는 조건이 존재합니다. 그러므로, $(i-1)^{th}$의 색이 $(i-2)^{th}$의 색과 다를 경우에만 $i^{th}$를 $(i-1)^{th}$와 같은 색으로 칠할 수 있습니다.

그렇다면, $(i-1)^{th}$ 포스트를 $(i-2)^{th}$ 포스트와 다른 색으로 칠하는 방법은 몇 개나 될까요? 첫 번째 옵션에서 언급했듯이, $(i-1)^{th}$ 포스트와 다른 색으로 $i^{th}$ 포스트를 칠하는 방법이 `(k - 1) * totalWays(i - 1)`개 존재하므로, $(i-1)^{th}$ 포스트를 $(i-2)^{th}$ 포스트와 다른 색으로 칠하는 방법은 `1 * (k - 1) * totalWays(i - 2)`개 존재합니다.

위의 두가지 시나리오를 합치면 `totalWays(i) = (k - 1) * totalWays(i - 1) + (k - 1) * totalWays(i - 2)`가 도출되고 정리하면,

`totalWays(i) = (k - 1) * (totalWays(i - 1) + totalWays(i - 2))`가 됩니다.

이것이 베이스 케이스로부터 문제를 풀기위해 도출한 recurrence relation 입니다.

## Approach 1: Top-Down DP
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            
            # Check if we have already calculated totalWays(i)
            if i in memo:
                return memo[i]
            
            # Use the recurrence relation to calculate total_ways(i)
            memo[i] = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
            return memo[i]

        memo = {}
        return total_ways(n)
```
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        def total_ways(i):
            if i == 1: 
                return k
            if i == 2: 
                return k * k
            
            return (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
        
        return total_ways(n)
```

## Approach 2: Bottom-Up DP
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        # Base cases for the problem to avoid index out of bound issues
        if n == 1:
            return k
        if n == 2:
            return k * k

        total_ways = [0] * (n + 1)
        total_ways[1] = k
        total_ways[2] = k * k
        
        for i in range(3, n + 1):
            total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])
        
        return total_ways[n]
```

### Complexity Analysis
- Time: $O(n)$
- Space: $O(n)$