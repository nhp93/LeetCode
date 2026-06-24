class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        max_curr = min_curr = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        total = 0
        for num in nums:
            total += num
            max_curr = max(num, max_curr + num)
            if max_curr > max_sum:
                max_sum = max_curr
            min_curr = min(num, min_curr + num)
            if min_curr < min_sum:
                min_sum = min_curr
        if total < 0:
            return max_sum
        return max(max_sum, total - min_sum)
