class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        dic = {w:i for i, w in enumerate(words)}
        
        for i1, w1 in enumerate(words):
            for m in range(len(w1) + 1):
                left_part = w1[:m]
                right_part = w1[m:]
                if left_part == left_part[::-1]:
                    if right_part[::-1] in dic and dic[right_part[::-1]] != i1:
                        res.append([dic[right_part[::-1]], i1])
                if right_part == right_part[::-1] and m < len(w1): #second condition also help making sure no duplicate
                    if left_part[::-1] in dic and dic[left_part[::-1]] != i1:
                        res.append([i1, dic[left_part[::-1]]])
        return res