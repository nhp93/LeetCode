class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        converted_list = [0] + list(accumulate(x % 2 for x in nums))
        count = Counter(converted_list)

        for key in count:
            if (key - k) in count:
                if k > 0:
                    res += count[key] * count[key - k]
                else:
                    res += count[key] * (count[key] - 1) // 2
        return res