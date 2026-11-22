# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None

        self.dfs(root)

        return self.result
        
    def dfs(self, node):
        if node is None or self.result is not None:
            return

        self.dfs(node.left)
        if self.result is not None:
            return
        
        self.k -= 1
        if self.k == 0:
            if self.result is None:
                self.result = node.val
            return
        
        self.dfs(node.right)
