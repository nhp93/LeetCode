class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = 0
        counts = Counter(words)
        mid = False
        for word in counts:
            if word[::-1] == word:
                if counts[word] % 2 == 0:
                    count += counts[word] * 2
                else:
                    count += (counts[word] - 1) * 2
                    mid = True
            else:
                if word[::-1] in counts:
                    count += min(counts[word], counts[word[::-1]]) * 4
                    counts[word] = 0
                    counts[word[::-1]] = 0
        if mid:
            count += 2
        return count