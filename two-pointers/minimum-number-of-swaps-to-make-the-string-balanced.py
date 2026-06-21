class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in range (len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == '[':
                stack.append(s[i])
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
        
        l = len(stack)
        if l % 4 == 0:
            return int (l / 4)
        else:
            return (l // 4) + 1
            
            