class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        window_sum = 0
        finding = float('inf')
        for i in range(0, len(nums)):
            window_sum += nums[i]
            while window_sum >= target:
                finding = min(finding, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
            right += 1
        if finding != float('inf'):
            return finding
        return 0