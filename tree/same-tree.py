# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            if tree1.val != tree2.val:
                return False
            left1, left2 = tree1.left, tree2.left
            right1, right2 = tree1.right, tree2.right
            left_same = dfs(left1,left2)
            right_same = dfs(right1,right2)
            return left_same and right_same
        return dfs(p,q)