from typing import Optional, TreeNode, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return None
        stack = [(False, root)]; acc = []
        while stack:
            flag, val = stack.pop()
            if val:
                if not flag:
                    stack.append((False, val.right))
                    stack.append((True, val))
                    stack.append((False, val.left))
                else:
                    acc.append(val.val)
        return acc
                    
        