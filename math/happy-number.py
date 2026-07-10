class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            for char in str(n):
                total += int(char) ** 2
            n = total
        return n == 1