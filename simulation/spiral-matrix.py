class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        right = len(matrix[0])
        bot = len(matrix)

        total = (right) * (bot)

        lst = []
        while top < bot and left < right:
            for a in range (left, right):
                lst.append(matrix[top][a])
            top += 1
            for b in range (top, bot):
                lst.append(matrix[b][right - 1])
            right -= 1
            if not (top < bot and left < right):
                break
            for c in range (right - 1,left - 1, - 1):
                lst.append(matrix[bot - 1][c])
            bot -= 1
            for d in range (bot - 1, top - 1, -1):
                lst.append(matrix[d][left])
            left += 1
        return lst