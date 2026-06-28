class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        if k >= n:
            return "0"
        for i in range(n):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        if k > 0:
            stack = stack[:-k]
        res = "".join(stack).lstrip("0")
        return res if res else "0"