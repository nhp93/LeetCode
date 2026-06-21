class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        count = 0
        for i in range (0, len(nums) - 2):
            if sortedList[i] == 0:
                continue
            r = i + 2
            
            for l in range (i + 1, len(nums) - 1):
                while r < len(nums) and sortedList[i] + sortedList[l] > sortedList[r]:
                    r += 1
                count += (r - l - 1)
        return count
