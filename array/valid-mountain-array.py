class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        max = arr[0]
        j = 0
        if len(arr) < 3:
            return False
        for i in range (len(arr)):
            if arr[i] > max:
                max = arr[i]
                j = i
        if j == 0 or j == len(arr)-1:
            return False
            
        for m in range(0,j):
            if arr[m] >= arr[m+1]:
                return False
        for n in range(j,len(arr)-1):
            if arr[n] <= arr[n+1]:
                return False
        return True
            
        