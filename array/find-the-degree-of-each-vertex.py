class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for mat in matrix:
            res.append(sum(mat))
        return res