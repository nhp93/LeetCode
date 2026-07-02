# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)
        even, odd = even_dummy, odd_dummy

        curr = head
        count = 1
        while curr:
            if count % 2 == 1:
                odd.next = curr
                odd = odd.next
                count += 1
            else:
                even.next = curr
                even = even.next
                count += 1
            curr = curr.next
        
        even.next = None
        odd.next = even_dummy.next
        return odd_dummy.next
            

        # even_dummy = ListNode(0)
        # odd_dummy = ListNode(0)
        # even, odd = even_dummy, odd_dummy
        
        # curr = head
        # while curr:
        #     if curr.val % 2 == 0:
        #         even.next = curr
        #         even = even.next
        #     else:
        #         odd.next = curr
        #         odd = odd.next
        #     curr = curr.next
        # even.next = None
        # odd.next = even_dummy.next
        # return odd_dummy.next