# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, node, depth=0):
        if not node:
            return depth
        
        l = self.dfs(node.left, depth + 1)
        r = self.dfs(node.right, depth + 1)

        return max(l, r)

# root = [1, 2,3, null,null,4,null]
# dfs(1, 0)
# dfs(2, 1)
# dfs(null, 2), return 2
# dfs(2, 1), l=2
# dfs(null, 2), return 2
# dfs(2, 1), l=2, r=2, return 2
# dfs(1, 0), l=2
# dfs(3, 1)
# dfs(4, 2)
# dfs(null, 3)
# dfs(4, 2), l=3
# dfs(null, 3), r=3
# dfs(4, 2), l=3, r=3, return 3
# dfs(3, 1), l=3
# dfs(null, 2), return 2
# dfs(3, 1), l=3, r=2, return 3
# dfs(1, 0), l=2, r=3, return 3
