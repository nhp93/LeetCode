class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maxCount = -1
        while right < len(nums):
            count = right - left
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            count = right - left + 1
            maxCount = max(count, maxCount)
            right += 1
        return maxCount