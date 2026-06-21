class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for i in range(1, n + 1):
            res = sum(int(digit) for digit in str(i))
            d[res] += 1
        max_val =  max(d.values())
        count = 0
        for val in d.values():
            if val == max_val:
                count += 1
        return count