class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = []
        left_sum = 0
        right_sum = sum(nums) - nums[0]
        total = sum(nums)
        ans = []
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            left_diff = nums[i]*i - left_sum
            right_diff = right_sum - nums[i]*(len(nums) - i - 1)

            ans.append(left_diff + right_diff)

            left_sum += nums[i]
        return ans