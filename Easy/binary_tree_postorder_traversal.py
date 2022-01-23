from typing import Optional, TreeNode, List
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        
        stack = deque(); ans = deque()
        
        while True:
            while root:
                if root.right: stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right and len(stack) > 0 and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                root = None
            if len(stack) == 0: break
                
        return ans