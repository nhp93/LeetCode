class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d1 = Counter(nums1)
        # d2 = Counter(nums2)
        # res = []
        # for x in d1:
        #     if x in d2:
        #         res.append(x)
        # return res
        return list(set(Counter(nums1) & Counter(nums2)))