class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # m = len(mat)
        # n = len(mat[0])
        # row_count = [0] * m
        # col_count = [0] * n
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 1:
        #             row_count[r] += 1
        #             col_count[c] += 1
        # count = 0
        # for a in range(m):
        #     if row_count[a] == 1:
        #         for b in range(n):
        #             if mat[a][b] == 1 and col_count[b] == 1:
        #                 count += 1
        # return count

        m = len(mat)
        n = len(mat[0])
        count = 0
        for r in range(m):
            row_count = Counter(mat[r])
            if row_count[1] == 1:
                index_found = mat[r].index(1)
                col_count = Counter(mat[row][index_found] for row in range(m))
                if col_count[1] == 1:
                    count += 1
        return count