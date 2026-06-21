class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = ''.join(map(str, nums))
        parts = s.split('0')
        maxCount = 0
        for part in parts:
            if len(part) > maxCount:
                maxCount = len(part)
        
        return maxCount
