class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_max = len(matrix)
        col_max = len(matrix[0])
        for r in range(1, row_max):
            for c in range(1, col_max):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False

        return True


