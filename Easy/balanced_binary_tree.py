from typing import Optional, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if abs(self.height(root.right) - self.height(root.left)) > 1: return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
        
            