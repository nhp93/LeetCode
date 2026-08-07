# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        dq = deque([root])
        while dq:
            curr = dq.popleft()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        return root