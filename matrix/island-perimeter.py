class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for r in range (maxRow):
            for c in range (maxCol):
                if grid[r][c] == 1:
                    for dr, dc in DIRS: #chạy từng element trong tuple.
                        r1, c1 = r + dr, c + dc #new location of r and c to check 0 or 1
                        if r1 < 0 or c1 < 0:
                            count += 1
                        elif r1 == maxRow or c1 == maxCol:
                            count += 1
                        elif grid[r1][c1] != 1:
                            count += 1
                        
        return count
