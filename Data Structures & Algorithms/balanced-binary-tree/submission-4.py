# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        self.dfs(root)
        
        return self.balanced
    
    def dfs(self, node, level=0):
        if node is None:
            return level
        
        l = self.dfs(node.left, level + 1)
        p = self.dfs(node.right, level + 1)

        if abs(p - l) > 1:
            self.balanced = False
        
        return max(l, p)
