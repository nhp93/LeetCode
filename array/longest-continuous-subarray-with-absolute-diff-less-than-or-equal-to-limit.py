class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        max_leng = float('-inf')
        l = 0
        if len(nums) == 1:
            return 1
        for r in range(len(nums)):
            while min_dq and nums[min_dq[-1]] >= nums[r]:
                min_dq.pop()
            while max_dq and nums[max_dq[-1]] <= nums[r]:
                max_dq.pop()

            min_dq.append(r)
            max_dq.append(r)
            
            while abs(nums[min_dq[0]] - nums[max_dq[0]]) > limit:
                l += 1
                if min_dq[0] < l:
                    min_dq.popleft()
                if max_dq[0] < l:
                    max_dq.popleft()

            max_leng = max(max_leng, r - l + 1)
        return max_leng