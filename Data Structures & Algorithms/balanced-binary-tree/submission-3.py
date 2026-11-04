# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0

        self.dfs(root)

        return self.diff <= 1
    
    def dfs(self, node, depth=0):
        if not node: return depth

        l = self.dfs(node.left, depth + 1)
        r = self.dfs(node.right, depth + 1)
        
        self.diff = max(self.diff, max(l, r) - min(l, r))

        return max(l, r)
