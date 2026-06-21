class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        i = 0
        while i < len(nums):
            left += nums[i]
            right -= nums[i]
            nums[i] = abs(left - right - nums[i])
            i += 1
        return nums