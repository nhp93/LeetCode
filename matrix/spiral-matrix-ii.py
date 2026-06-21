class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = left = 0
        right = n
        bot = n
        total = (right) * (bot)
        lst = []
        i = 1
        mat = [[0] * n for _ in range(n)]
        while top < bot and left < right:
            for a in range (left, right):
                mat[top][a] = i
                i += 1
            top += 1
            for b in range (top, bot):
                mat[b][right - 1] = i
                i += 1
            right -= 1
            if not (top < bot and left < right):
                break
            for c in range (right - 1,left - 1, - 1):
                mat[bot - 1][c] = i
                i += 1
            bot -= 1
            for d in range (bot - 1, top - 1, -1):
                mat[d][left] = i
                i += 1
            left += 1
        return mat