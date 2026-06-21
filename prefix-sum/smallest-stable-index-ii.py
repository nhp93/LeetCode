class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        leng = len(nums)
        prefix_max = [nums[0]] * leng
        suffix_min = [nums[-1]] * leng
        for i in range(1, leng):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        for i in range(leng - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        for i in range(leng):
            if (prefix_max[i] - suffix_min[i]) <= k:
                return i
        return -1