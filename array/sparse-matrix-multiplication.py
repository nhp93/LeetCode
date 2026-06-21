class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for r1 in range(m):
            for c1 in range(k):
                if mat1[r1][c1] != 0:
                    for c2 in range(n):
                        res[r1][c2] += mat1[r1][c1] * mat2[c1][c2]
        return res
