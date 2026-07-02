# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        hash_map = {}
        stack = []
        curr = head
        while curr:
            value = curr.val
            if value not in hash_map:
                hash_map[value] = 0
            if not stack:
                stack.append(value)
            else:
                if value > stack[-1]:
                    while stack:
                        hash_map[stack.pop()] = value
                else:
                    stack.append(value)
            curr = curr.next

        res = []
        for val in hash_map.values():
            res.append(val)
        return res