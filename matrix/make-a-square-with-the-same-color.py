class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        s = 2
        for r in range(m-s+1):
            for c in range(m-s+1):
                counts = {'B': 0, 'W': 0}
                for r1 in range(r, r+s):
                    for c1 in range(c, c+s):
                        if grid[r1][c1] == 'B':
                            counts['B'] += 1
                        else:
                            counts['W'] += 1
                if counts['B'] >= 3 or counts['W'] >= 3:
                    return True
        return False