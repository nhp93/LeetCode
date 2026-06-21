class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = Counter(s)
        stack = []
        visited = set()
        for char in s:
            counts[char] -= 1
            if not stack:
                stack.append(char)
                visited.add(char)

            if char not in visited:
                if char < stack[-1]:
                    while len(stack) > 0 and char < stack[-1]:
                        if counts[stack[-1]] > 0:
                            visited.remove(stack.pop())
                        else:
                            break
                    stack.append(char)
                    visited.add(char)
                else:
                    stack.append(char)
                    visited.add(char)
        return "".join(stack)
            
