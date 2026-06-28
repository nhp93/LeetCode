class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        left = float('-inf')
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                left = num
            elif len(stack) == 1:
                if num > stack[-1]:
                    stack.append(num)
                elif num < stack[-1]:
                    stack.pop()
                    stack.append(num)
                    left = num
            elif len(stack) == 2:
                if num < stack[-1] and num > left:
                    return True
                if num > stack[-1]:
                    stack.pop()
                    stack.append(num)
                if num < left:
                    stack.pop()
                    stack.pop()
                    stack.append(num)
                    left = num
        return False