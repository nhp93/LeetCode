class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.extend(nums2)
        d = defaultdict(int)
        for (id_, v) in nums1:
            d[id_] += v
        return sorted([id_, v] for id_, v in d.items())