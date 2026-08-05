# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        while currA:
            currB = headB
            while currB:
                currB = currB.next
                if currA == currB:
                    return currA
            currA = currA.next
        return None
