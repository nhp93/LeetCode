class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            area = (r - l) * min(height[r], height[l])
            if area > maxA:
                maxA = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA