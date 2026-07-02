# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        count = 0
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
        
        curr = prev
        counts = 0
        while curr:
        #     if curr.next == None:
        #         curr.next = ListNode(1)
        #         curr.val = 0
        #     else:
        #         curr.val = 0
        #         curr = curr.next
        #         counts += 1
        # if count != counts:
        #     curr.val += 1
            if curr.val == 9:
                if curr.next == None:
                    curr.next = ListNode(1)
                    curr.val = 0
                    break
                else:
                    curr.val = 0
                    curr = curr.next
            else:
                curr.val += 1
                break
        
        head = prev
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev