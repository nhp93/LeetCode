class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        max_row = len(mat)
        max_col = len(mat[0])
        
        if r * c != max_row * max_col:
            return mat
        
        lst = []
        for row in range(max_row):
            for col in range(max_col):
                lst.append(mat[row][col])

        x = 0
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = lst[x]
                x += 1
        return res