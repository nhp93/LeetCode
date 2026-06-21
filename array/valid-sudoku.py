class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_seen = [[False] * n for _ in range(n)]
        col_seen = [[False] * n for _ in range(n)]
        box_seen = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                box_index = (r//3) * 3 + (c//3) #find postion of the box
                val = int(board[r][c]) - 1
                if row_seen[r][val] or col_seen[c][val] or box_seen[box_index][val]:
                    return False
                row_seen[r][val] = True
                col_seen[c][val] = True
                box_seen[box_index][val] = True
        return True