class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(c) for c in s]
        prefix_sum = list(accumulate(nums))
        suffix_sum = prefix_sum[-1]
        max_val = 0
        for i in range(len(s) - 1):
            zeros_left = i + 1 - prefix_sum[i]
            ones_right = suffix_sum - prefix_sum[i]
            max_val = max(zeros_left + ones_right, max_val)
        return max_val
