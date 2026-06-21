class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCount = 0
        maxIndex = 0
        m = len(mat)
        n = len(mat[0])
        for r in range(m):
            if sum(mat[r]) > maxCount:
                maxIndex = r
                maxCount = sum(mat[r])
        return [maxIndex, maxCount]