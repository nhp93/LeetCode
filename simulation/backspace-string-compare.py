class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for s1 in s:
            if s1 != "#":
                stack1.append(s1)
            else:
                if stack1:
                    stack1.pop()
        for s2 in t:
            if s2 != "#":
                stack2.append(s2)
            else:
                if stack2:
                    stack2.pop()
        return stack1 == stack2