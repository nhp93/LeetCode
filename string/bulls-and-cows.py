class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_count = 0
        cow_count = 0
        for s in range(len(secret)):
            if secret[s] == guess[s]:
                bull_count += 1

        sC = Counter(secret)
        gC = Counter(guess)

        for key in sC:
            if key in gC:
                cow_count += min(sC[key], gC[key])
        cow_count -=  bull_count

        return (str(bull_count) + "A" + str(cow_count) + "B")