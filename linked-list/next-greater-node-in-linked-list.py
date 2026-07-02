# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        res = [0] * len(nodes)
        stack = []

        for index, value in enumerate(nodes):
            while stack and value > stack[-1][1]:
                i, v  = stack.pop()
                res[i] = value
            stack.append((index, value))
        
        return res
