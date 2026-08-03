# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best_diameter = 0
        def dfs(node):
            left_height = right_height = 0
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.best_diameter = max(self.best_diameter, left + right)    
            return 1 + max(left, right)
        dfs(root)
        return self.best_diameter