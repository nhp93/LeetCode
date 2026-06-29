class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix_sum = list(accumulate(cardPoints))
        suffix_sum = list(accumulate(cardPoints[::-1]))
        print(prefix_sum)
        print(suffix_sum)
        max_sum = float('-inf')
        for i in range(k+1):
            if i == 0:
                total = prefix_sum[k-1]
                print(total)
                max_sum = max(max_sum, total)
            elif i == k:
                total = suffix_sum[k-1]
                max_sum = max(max_sum, total)
            else:
                total = prefix_sum[k-i-1] + suffix_sum[i-1]
                print(total)
                print("I")
                print(i)
                max_sum = max(max_sum, total)
        return max_sum