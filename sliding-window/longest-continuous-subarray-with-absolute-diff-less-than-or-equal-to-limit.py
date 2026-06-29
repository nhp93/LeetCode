class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dq = deque()
        max_leng = float('-inf')
        if len(nums) == 1:
            return 1
        for num in nums:
            if not dq:
                dq.append(num)
            else:
                while dq and abs(dq[0] - num) > limit:
                    dq.popleft()
                dq.append(num)
                max_leng = max(len(dq), max_leng)

        return max_leng