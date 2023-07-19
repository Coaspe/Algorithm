heights = []

for _ in range(int(input())):
    heights.append(int(input()))

stack = [-1]
max_area = 0
for i in range(len(heights)):
    while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
        current_height = heights[stack.pop()]
        current_width = i - stack[-1] - 1
        max_area = max(max_area, current_height * current_width)
    stack.append(i)

while stack[-1] != -1:
    current_height = heights[stack.pop()]
    current_width = len(heights) - stack[-1] - 1
    max_area = max(max_area, current_height * current_width)


print(max_area)
