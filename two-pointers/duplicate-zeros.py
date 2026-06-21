class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        right = len(arr) - 1
        count0 = 0
        a = 0
        i = 0
        n = len(arr)
        while i < n:
            if arr[a] == 0:
                if i == n - 1: 
                    arr[n - 1] = 0
                    n -= 1
                    break
                count0 += 1
                i += 1
            a += 1
            i += 1
        
        x = n - 1
        for i in range (a-1, -1, -1):
            if arr[i] != 0:
                arr[x] = arr[i]
                x -= 1
            else:
                arr[x] = 0
                if (x - 1 >= 0):
                    arr[x - 1] = 0
                x -= 2
            