class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                if heights[i] >= heights[stack[-1]]:
                    stack.append(i)
                else:
                    left = 0
                    right = stack[-1]
                    while stack and heights[stack[-1]] > heights[i]:
                        left = stack.pop()
                    area = (i-left) * heights[left]
                    if area > max_area:
                        max_area = area
                    stack.append(i)
        while stack:
            h = heights[stack.pop()]
            if not stack:
                w = n
            else:
                w = n - stack[-1] - 1
            max_area = max(max_area, h * w)
        return max_area