class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        lst = []
        for i in range (len(nums)):
            s.add(nums[i])
        for j in range (1, len(nums) + 1):
            if j not in s:
                lst.append(j)
        return lst
        