class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = deque(num)
        stack = deque()

        if k >= len(num):
            return "0"

        while num:
            n = int(num.popleft())

            while stack and stack[-1] > n and k:
                k -= 1
                stack.pop()

            while stack and stack[0] == 0:
                stack.popleft()

            stack.append(n)

        while k and stack:
            stack.pop()
            k -= 1

        return "".join(str(n) for n in list(stack)) if stack else "0"
