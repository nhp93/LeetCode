class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        cond  = True
        n = len(grid)
        for r in range(n):
            if grid[r][r] == 0 or grid[r][n-r-1] == 0:
                return False
            for c in range(n):
                if grid[r][c] != 0 and (r!=c and c!= n-r-1):
                    return False
        return cond