# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_seen = set()
        current = head
        while current is not None:
            if current in node_seen:
                return True
            node_seen.add(current)
            current = current.next
        return False
        