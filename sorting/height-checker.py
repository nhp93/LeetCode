class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        idealList = sorted(heights)
        count = 0 
                
        for c in range(len(heights)):
            if heights[c] != idealList[c]:
                count += 1
        return count
        