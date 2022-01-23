# Definition for a binary tree node.
from typing import Optional, TreeNode, List
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        
        stack = deque(); ans = []
        
        while True:
            while root:
                if root.left: stack.append(root.left)
                stack.append(root)
                root = root.right
            root = stack.pop()
            if root.left and len(stack) > 0 and stack[-1] == root.left:
                stack.pop()
                stack.append(root)
                root = root.left
            else:
                ans.append(root.val)
                root = None
            if len(stack) == 0: break
        return ans[::-1]