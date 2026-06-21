class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        long sum = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c <grid[0].length; c++) {
                sum += grid[r][c];
            }
        }

        long sumRow = 0;
        for (int r = 0; r < grid.length; r++) {
            if (sumRow * 2 != sum) {
                for (int c = 0; c <grid[0].length; c++) {
                    sumRow += grid[r][c];
                }
            }
            else {
                return true;
            }
        }

        long sumCol = 0;
        for (int c = 0; c < grid[0].length; c++) {
            if (sumCol * 2 != sum) {
                for (int r = 0; r <grid.length; r++) {
                    sumCol += grid[r][c];
                }
            }
            else {
                return true;
            }
        }
        return false;
    }
}