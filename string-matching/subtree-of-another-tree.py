# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(sub_root, subRoot):
            if sub_root is None and subRoot is None:
                return True
            elif sub_root is None or subRoot is None:
                return False
            elif sub_root.val == subRoot.val:
                left_same = dfs(sub_root.left, subRoot.left)
                right_same = dfs(sub_root.right, subRoot.right)
                if left_same and right_same:
                    return True
            l = dfs(sub_root.left, subRoot)
            r = dfs(sub_root.right, subRoot)
            return l or r
        return dfs(root, subRoot)