class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m = len(mat)
        for i in range(4):
            if mat == target:
                return True
            for r in range(m):
                for c in range(r+1, m):
                    mat[r][c], mat[c][r]= mat[c][r], mat[r][c]
        
            for r1 in range(m):
                left = 0
                right = m-1
                while (left < right):
                    mat[r1][left], mat[r1][right] = mat[r1][right], mat[r1][left]
                    left += 1
                    right -= 1
        return False      