# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        if count == n:
            return None
        curr = head
        pos = 0
        while curr:
            pos += 1
            if pos == count - n:
                curr.next = curr.next.next

            curr = curr.next
        return head
