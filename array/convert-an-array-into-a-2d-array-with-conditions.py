class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_counter = Counter(nums)
        max_row = max(nums_counter.values())
        res = [[] for _ in range(max_row)]
        for key, freq in nums_counter.items():
            i = 0
            while(i < freq):
                res[i].append(key)
                i += 1
        return res