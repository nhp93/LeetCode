class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dom = []
        for a,b in dominoes:
            val = min(a, b) * 10 + max(a, b)
            dom.append(val)
        
        count = 0
        s = Counter(dom)
        for key in s:
            if s[key] > 1:
                count += math.comb(s[key],2)
        return count
        
            