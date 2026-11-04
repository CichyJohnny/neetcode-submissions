# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) != (q is None): return False

        return self.dfs(p, q)
        
    def dfs(self, p, q):
        if not p and not q: return True

        if p.val != q.val: return False
        if (p.left is None) != (q.left is None): return False
        if (p.right is None) != (q.right is None): return False

        return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
