class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        flips = 0
        n = len(nums)
        dq = deque()
        flips = 0
        for i in range(n):
            if dq and dq[0] == i:
                dq.popleft()
            
            if nums[i] == 0 and len(dq) % 2 == 0 or nums[i] == 1 and len(dq) % 2 == 1:
                if  i + k > len(nums):
                    return -1
                    
                dq.append(i+k)
                flips += 1
            
        return flips

                # if i + k > n:
                #     return -1
                # for m in range(k):
                #     if nums[i + m] == 1:
                #         nums[i + m] = 0
                #     else:
                #         nums[i + m] = 1
                # flips += 1
        return flips