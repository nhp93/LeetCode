class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        set_nums = set(nums)
        count = 0
        for key in set_nums:
            count += ((key - diff) in set_nums and (key + diff) in set_nums)
        return count