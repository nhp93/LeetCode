class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        res = set()
        hash_map = Counter(nums)
        if k == 0:
            return sum(1 for ke in hash_map if hash_map[ke] > 1)
        for key in hash_map:
            if k + key in hash_map:
                res.add((key, (k + key)))
        print(res)
        return len(res)


