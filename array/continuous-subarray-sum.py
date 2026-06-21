class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        seen_dict = {0:-1}
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in seen_dict:
                if i - seen_dict[prefix_mod] >= 2:
                    return True
            else:
                seen_dict[prefix_mod] = i
        return False
