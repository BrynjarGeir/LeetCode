# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        integers = []
        root = TreeNode()
        root.left = root1; root.right = root2
        
        def getAllIntegers(root):
            if root.left:
                integers.append(root.left.val)
                getAllIntegers(root.left)
            if root.right:
                integers.append(root.right.val)
                getAllIntegers(root.right)
        
        getAllIntegers(root)
                
        return sorted(integers)