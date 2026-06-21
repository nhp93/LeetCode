class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] % 2 != 0:
                right -= 1
            else:
                if nums[left] % 2 == 1:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    left += 1
        return nums


        