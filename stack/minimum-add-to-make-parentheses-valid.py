class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for p in range(len(s)):
            if not stack:
                if s[p] == ")":
                    count += 1
                else:
                    stack.append("(")
            else:
                if s[p] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                else:
                    stack.append("(")
        return count + len(stack)