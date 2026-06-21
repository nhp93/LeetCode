class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        total = 0
        for v in numsCount.values():
            if v > 1:
                total += (v * (v - 1)) // 2
        return total