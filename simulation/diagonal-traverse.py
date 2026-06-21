class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i = 0
        res = []
        up = True
        row = 0
        col = 0
        n = len(mat)
        m = len(mat[0])
        while i < n*m:
            if up:
                if col == m-1:
                    res.append(mat[row][col])
                    row += 1
                    up = False
                elif row == 0:
                    res.append(mat[row][col])
                    col += 1
                    up = False
                else:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                if row == n-1:
                    res.append(mat[row][col])
                    col += 1
                    up = True
                elif col == 0:
                    res.append(mat[row][col])
                    row += 1
                    up = True
                else:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1

            i += 1
        return res
