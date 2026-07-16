'''
Input: 2 strings
Output: character that is the difference btw 2 strings
Edge Cases: len(t) <= len(s): 
len(s) == 0: return t

Planning:
Using Counter for both string s and t
Return the different between 2 dictionaries

counter_t = {
    "a": 1
    "b": 1
    "c": 1
    "d": 1
    "e": 1
}
abcdeabcd
counter_s = {
    "a": 1
    "b": 1
    "c": 1
    "d": 1
}
adbcacbd
'''
class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) <= len(s):
            return
        counter_s = Counter(s)
        counter_t = Counter(t)
        for key in counter_t:
            if counter_t[key] > counter_s[key]:
                return key
    
        

        