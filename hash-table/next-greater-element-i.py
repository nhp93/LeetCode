class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        hash_map = defaultdict(int)
        for i in range(len(nums2) - 1):
            num1 = nums2[i]
            num2 = nums2[i+1]
            stack.append(num1)
            if num1 < num2:
                while stack:
                    hash_map[stack.pop()] = num2
        
        for num in nums1:
            if hash_map[num] > 0:
                res.append(hash_map[num])
            else:
                res.append(-1)
        
        return res
