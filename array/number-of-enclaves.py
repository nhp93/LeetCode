class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or r == m-1:
                        grid[r][c] = 2
                    elif c == 0 or c == n-1:
                        grid[r][c] = 2

        changing = True            
        while changing:
            changing = False
            for r1 in range(1, m-1):
                for c1 in range(1, n-1):
                    if grid[r1][c1] == 1:
                        if grid[r1+1][c1] == 2 or grid[r1-1][c1] == 2:
                            grid[r1][c1] = 2
                            changing = True
                        elif grid[r1][c1+1] == 2 or grid[r1][c1-1] == 2:
                            grid[r1][c1] = 2
                            changing = True
        
        count = 0
        for r2 in range(1, m-1):
            for c2 in range(1, n-1):
                if grid[r2][c2] == 1:
                    count += 1
        return count

