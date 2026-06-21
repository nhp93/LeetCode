class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(1, len(nums) + 1):
            diff = max(nums[:i]) - min(nums[i-1:])
            if diff <= k:
                return i - 1
        return -1