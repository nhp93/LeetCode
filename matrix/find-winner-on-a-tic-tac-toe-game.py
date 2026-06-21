class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        board = [[0] * n for _ in range(n)]
        
        def checkRow(row, player):
            for col in range(n):
                if board[row][col] != player:
                    return False
            return True
        
        def checkCol(col, player):
            for row in range(n):
                if board[row][col] != player:
                    return False
            return True
        
        def checkDownDiagonal(player):
            for row in range(n):
                if board[row][row] != player:
                    return False
            return True
        
        def checkUpDiagonal(player):
            for row in range(2, -1, -1):
                if board[row][2-row] != player:
                    return False
            return True

        player = 1
        for r, c in moves:
            board[r][c] = player
            if (checkRow(r, player) or checkCol(c, player) or checkDownDiagonal(player) or checkUpDiagonal(player)):
                if player == 1:
                    return "A"
                else:
                    return "B"
            player = 3 - player
        for row in range(n):
            for col in range(n):
                if board[row][col] == 0:
                    return "Pending"
        return "Draw"