class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        newList = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                newList.append(nums[i])
            else:
                zero_count += 1
        for i in range(zero_count):
            newList.append(0)
        
        for i in range(len(nums)):
            nums[i] = newList[i]
        return nums
        
        