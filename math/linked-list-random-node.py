# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        lst = []
        curr = self.head
        while curr:
            value = curr.val
            curr = curr.next
            lst.append(value)
        

        return lst[random.randint(0, len(lst) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()