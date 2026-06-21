class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        total = sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            if prefix_sum[i] >= total - prefix_sum[i]:
                count += 1
        return count