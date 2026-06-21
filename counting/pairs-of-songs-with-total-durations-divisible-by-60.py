class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # count = 0
        # for i in range(len(time) - 1):
        #     for j in range(i + 1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             print(i, j)
        #             count += 1
        # return count

        time = [i % 60 for i in time]
        counts = Counter(time)
        count = 0

        for k in counts:
            if k == 30 or k == 0:
                count += math.comb(counts[k], 2)
            elif k < 30 and (60 - k) in counts:
                count += counts[k] * counts[60 - k]

        return count