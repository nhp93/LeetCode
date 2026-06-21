class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        for i in range (l):
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return - 1