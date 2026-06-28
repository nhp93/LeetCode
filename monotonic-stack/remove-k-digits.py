class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        if k == n:
            return "0"
        for i in range(n):
            if not stack:
                stack.append(num[i])
            else:
                if k > 0:
                    if num[i] < stack[-1]:
                        stack.pop()
                        stack.append(num[i])
                        k -= 1
                    else:
                        stack.append(num[i])
                else:
                    stack.append(num[i])
        if k > 0:
            stack = stack[:-k]
        res = "".join(stack)
        return str(int(res))