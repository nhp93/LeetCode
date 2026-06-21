class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        return [k for k, v in dic.items() if v > len(nums) // 2][0]