class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        min_avg = float('inf')
        total = sum(nums)
        min_index = 0
        for i in range(len(nums)):
            left_avg = prefix_sum[i]//(i+1)
            if i != len(nums) - 1:
                right_avg = (total - prefix_sum[i]) // (len(nums) - i - 1)
                diff = abs(left_avg - right_avg)
            else:
                diff = abs(left_avg)
            if diff < min_avg:
                min_avg = diff
                min_index = i
        return min_index