class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] > nums[i+1]:
                nums[i+1] = nums[i+1] + nums[i+2]
                count += 1
        return count