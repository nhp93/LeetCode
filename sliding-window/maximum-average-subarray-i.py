class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_sum = list(accumulate(nums))
        n = len(nums)
        max_sum = prefix_sum[k-1]
        for i in range(k, n):
            curr = prefix_sum[i] - prefix_sum[i-k]
            max_sum = max(max_sum, curr)
        return max_sum / k
            