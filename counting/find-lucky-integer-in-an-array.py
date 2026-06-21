class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}
        maxL = -1
        for i in arr:
            if i not in dict.keys():
                dict[i] = 0
            dict[i] += 1
        for num, count in dict.items():
            if num == count:
                maxL = max(maxL, num)
        return maxL


