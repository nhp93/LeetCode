class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenList = []
        oddList = []
        for i in range (len(nums)):
            if i % 2 == 1:
                oddList.append(nums[i])
            else:
                evenList.append(nums[i])
        oddList.sort(reverse = True)
        evenList.sort()
        for j in range (len(nums)):
            if j % 2 == 1:
                nums[j] = oddList[j//2]
            else:
                nums[j] = evenList[j//2]
        return nums
