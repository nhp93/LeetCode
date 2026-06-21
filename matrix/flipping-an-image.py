class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for r in range(n):
            left = 0
            right = n - 1
            while (left <= right):
                if image[r][left] == image[r][right]:
                    if image[r][right] == 0:
                        image[r][right] = 1
                        image[r][left] = 1
                    else:
                        image[r][right] = 0
                        image[r][left] = 0
                left += 1
                right -= 1
        return image