class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_curr = 0
        chunks = 0
        for i in range(len(arr)):
            if arr[i] > max_curr:
                max_curr = arr[i]
            if max_curr == i:
                chunks += 1
        return chunks
