class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while j < len(popped):
            if stack:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    if i < len(pushed):
                        stack.append(pushed[i])
                        i += 1
                    else:
                        return False
            else:
                stack.append(pushed[i])
                i += 1
            
            
        
        if i == j == len(pushed):
            return True
        return False