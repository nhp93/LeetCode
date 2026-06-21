class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lst = []
        for row in grid:
            for val in row:
                lst.append(val)
        r = lst[0] % x
        for val in lst:
            if val % x != r:
                return -1
        lst.sort()
        median = lst[len(lst) // 2]
        res = 0
        for val in lst:
            res += abs(val - median) // x
        return res