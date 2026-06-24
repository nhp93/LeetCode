class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        flips = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                if i + k > n:
                    return -1
                for m in range(k):
                    if nums[i + m] == 1:
                        nums[i + m] = 0
                    else:
                        nums[i + m] = 1
                
                flips += 1
                
        return flips