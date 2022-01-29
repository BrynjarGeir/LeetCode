# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def findAllValues(root):
            values.append(root.val)
            if root.left: findAllValues(root.left)
            if root.right: findAllValues(root.right)
        
        values = []
        
        findAllValues(root)
        
        values.sort()
        
        mindiff = inf
        
        for i in range(1, len(values)):
            mindiff = min(mindiff, abs(values[i] - values[i-1]))
            
        return mindiff