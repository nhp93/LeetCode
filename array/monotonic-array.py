class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increasing = True
        decreasing = True
        if n <= 2:
            return True
        else:
            for i in range(1,n):
                if nums[i-1] < nums[i]:
                    decreasing = False
                elif nums[i-1] > nums[i]:
                    increasing = False
        if increasing == True or decreasing == True:
            return True
        return False

