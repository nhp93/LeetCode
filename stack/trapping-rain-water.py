class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        left_wall = 0
        for h in height:
            if h < left_wall:
                stack.append(h)
            else:
                while stack:
                    area += (left_wall - stack.pop())
                    print(area)
                left_wall = h
        right_wall = 0
        while stack:
            h = stack.pop()
            if h > right_wall:
                right_wall = h
            else:
                area += (right_wall - h)
        return area
                    