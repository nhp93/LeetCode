class Solution:
    def find_max(self, grid, x, y):
        max_value = 0
        for i in range(x, x+3):
            for j in range(y, y+3):
                max_value = max(grid[i][j], max_value)
        return max_value

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_mat = [[0]  * (n-2) for _ in range(n-2)]
        for r in range(0, n-2):
            for c in range(0, n-2):
                max_mat[r][c] = self.find_max(grid, r, c)
        return max_mat