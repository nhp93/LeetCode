class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # l = len(words)
        # leng = len(words[0])
        # i = 0
        # res = []
        # while i < leng:
        #     cond = True
        #     for j in range (1, l):
        #         if words[0][i] not in words[j]:
        #             cond = False
        #     if cond == True:
        #         res.append(words[0][i])
        #         for k in range (1, l):
        #             words[k] = words[k].replace(words[0][i], '', 1)
        #     i += 1
        # return res

        common_letter = Counter(words[0])
        for word in words[1:]:
            letter_freq = Counter(word)
            for key in common_letter:
                common_letter[key] = min(common_letter[key], letter_freq[key])
        return list(common_letter.elements())
    