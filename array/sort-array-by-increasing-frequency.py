class Solution:

  def frequencySort(self, nums: List[int]) -> List[int]:
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 0
        dic[num] += 1

    sorted_items = sorted(dic.items(), key=lambda item: (item[1], -item[0]))

    res = []
    for k, v in sorted_items:
        for i in range(v):
            res.append(k)
    return res