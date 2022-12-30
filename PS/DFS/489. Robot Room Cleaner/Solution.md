# Solution

## Approach 1: Spiral Backtracking

### Concepts to use

두 가지 프로그래밍 컨셉이 있습니다.

> 첫 번째는 _제한된 프로그래밍_ 입니다.

제한된 프로그래밍은 기본적으로 각 로봇의 움직임 이후에 제한을 둔다는 것을 의미합니다.
로봇이 움직이고 해당 셀은 `visited`로 마크됩니다.
그것이 _제한_ 을 전파하고 고려해야할 조합의 수를 줄여줍니다.

![Constraints](https://leetcode.com/problems/robot-room-cleaner/solutions/265763/Figures/489/489_constraints.png)

> 두 번째는 _백트래킹_ 입니다.

몇 번의 움직임 이후에 로봇이 방문한 셀들로 둘러싸인다고 가정해봅시다.
하지만 해당 셀 이전에 다른 경로로 움직일 수 있는 대안이 존재합니다.
해당 경로는 사용, 청소되지 않았습니다. 이 시점에서 _백트래킹_ 을 수행합니다.
여기에서 _백트래킹_ 이란, 해당 셀로 돌아와서 대안이 되는 경로를 탐색하는 것을 의미합니다.

![Backtrack](https://leetcode.com/problems/robot-room-cleaner/solutions/265763/Figures/489/489_backtrack.png)

### Intuition

이 솔루션은 미로를 해결하는 방법인 우수법과 같은 아이디어를 기반으로 합니다.
앞으로 나아가서 셀을 `visited`로 마크하고 모든 셀을 청소합니다.
장애물을 만나면 _turn right_ 후 앞으로 나아갑니다.
항상 _turn right_ 후에 **앞으로 나아가야**합니다.
이미 방문한 셀은 가상의 장애물로 간주합니다.

> 오른쪽으로 턴 한 후에 장애물이 앞에 있으면 어떡하죠?

_Turn right_ 를 다시 수행합니다.

> 셀에서 대안이 되는 경로를 어떻게 탐색하나요?

해당 셀로 돌아가고 마지막으로 탐색한 방향에서 _turn right_를 수행합니다.

> 언제 멈추나요?

모든 가능한 경로를 탐색했을 때 정지합니다.
방문한 각 셀에 대해 모든 `4` 방향(위, 오른쪽, 아래, 왼쪽)을 선택합니다.

### Algorithm

백트래킹 함수인 `backtrack(cell = (0, 0), direction = 0)`의 알고리즘을 작성할 시간입니다.

- 셀을 `visited`로 마크하고 청소합니다.
- `4` 방향을 탐색합니다: `위`, `오른쪽`, `밑`, 그리고 `왼쪽` (오른쪽으로 회전하는 것이 기본 아이디어이기 때문에 순서가 중요합니다):
    - 선택된 방향에서 다음 셀을 확인합니다:
        - 아직 방문되지 않았고, 장애물이 없다면:
            - 앞으로 나아갑니다.
            - `backtrack(new_cell, new_direction)`로 다음 셀을 탐색합니다.
            - **백트래킹**, 즉 이전 셀로 돌아갑니다.
        - 앞에 가상 또는 실제 장애물이 있기 때문에 _turn right_ 합니다.

### Implementation

![Implementation](https://leetcode.com/problems/robot-room-cleaner/solutions/265763/Figures/489/489_implementation.png)

```python
class Solution:       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])
                
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()
    
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
```

### Complexity Analysis

- 시간 복잡도: $O(N-M)$, $N$은 방에 있는 셀의 수이고 $M$은 장애물의 수
    - 장애물이 아닌 셀을 단 한번만 방분합니다.
    - 각 방문에서 셀의 4 방향을 확인합니다. 그러므로, 총 명령의 수는 $4*(N-M)$ 입니다.
- 공간 복잡도: $O(N-M)$, $N$은 방에 있는 셀의 수이고 $M$은 장애물의 수
    - 장애물이 아닌 셀의 방문 여부를 해쉬 테이블을 사용하여 저장합니다.