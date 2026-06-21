class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = []
        for r in range(rows):
            rr = []
            for c in range(cols):
                total, count = 0, 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < rows and 0 <= j < cols:
                            total += img[i][j]
                            count += 1
                rr.append(total // count)
            res.append(rr)
        return res