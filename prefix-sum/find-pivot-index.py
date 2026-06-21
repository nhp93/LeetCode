class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        s = sum(nums)
        for i, v in enumerate(nums):
            if left_sum == (s - left_sum - v):
                return i
            left_sum += v
        return -1
