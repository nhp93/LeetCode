class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        right = float('-inf')
        stack = []
        if len(nums) < 3: return False
        min_prefix = [0] * len(nums)
        min_prefix[0] = nums[0]
        for i in range(1, len(nums)):
            min_prefix[i] = min(min_prefix[i-1], nums[i])

        for j in range(len(nums)-1,-1,-1):
            if nums[j] > min_prefix[j]:
                while stack and stack[-1] <= min_prefix[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
                

        return False