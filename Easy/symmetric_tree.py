from typing import Optional, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(left, right):
            if not left and not right: return True
            if left and right and left.val == right.val:
                return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
            return False
        return isSymmetric(root, root)
        