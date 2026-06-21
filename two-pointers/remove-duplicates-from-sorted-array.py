class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[left_pointer] = nums[i]
                left_pointer += 1
        return left_pointer