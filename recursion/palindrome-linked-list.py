# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        n = len(res)
        l,r  = 0, n-1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True