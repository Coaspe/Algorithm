from heapq import heappush, heappop


class MinStack:

    def __init__(self):
        self.stack = []
        self.heapq = []
        self.lazy = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.heapq, val)

    def pop(self) -> None:
        n = self.stack.pop()
        if n == self.heapq[0]:
            heappop(self.heapq)
        else:
            self.lazy[n] += 1

        while self.heapq and self.lazy[self.heapq[0]]:
            self.lazy[heappop(self.heapq)] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heapq[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
