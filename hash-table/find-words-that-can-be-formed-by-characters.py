class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCount = Counter(chars)
        total = 0

        for word in words:
            wordCount = Counter(word)
            state = True

            for k, v in wordCount.items():
                if v > charsCount[k]:
                    state = False
                    break

            if state == True:
                total += len(word)
        return total
