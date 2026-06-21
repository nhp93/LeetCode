class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        total = 0
        for r in range (l):
            total += mat[r][r]
            total += mat[l-r-1][r]
        if l % 2 == 0:
            return total
        f = int(l/2)
        return total - mat[f][f]
