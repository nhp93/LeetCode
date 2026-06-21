class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        sets = [first_row, second_row, third_row]
        res = []
        for word in words:
            for s in sets:
                if all(char in s for char in word.lower()):
                    res.append(word)
        return res