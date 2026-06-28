class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        hash_map = {}
        for i in range(len(nums2)):
            num2 = nums2[i]
            while stack and num2 > stack[-1]:
                hash_map[stack.pop()] = num2
            stack.append(num2)
        
        for num in nums1:
            if num in hash_map:
                res.append(hash_map[num])
            else:
                res.append(-1)
        
        return res
