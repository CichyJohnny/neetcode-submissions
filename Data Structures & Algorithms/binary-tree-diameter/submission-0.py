# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0

        self.dfs(root)
        return self.maxx
    
    def dfs(self, node, depth = 0):
        if not node: return depth

        l = self.dfs(node.left, depth + 1)
        r = self.dfs(node.right, depth + 1)

        self.maxx = max(self.maxx, l + r - 2 * (depth + 1))
        
        return max(l, r)

# root = [1, null,2, null,null,3,4, null,null,null,null,5,null,null,null]
# dfs(1, 0)
# dfs(null, 1), return 1
# dfs(1, 0), l=1
# dfs(2, 1)
# dfs(3, 2)
# dfs(5, 3)
# dfs(null, 4), return 4
# dfs(5, 3), l=4
# dfs(null, 4), return 4
# dfs(5, 3), l=4, r=4, return 4, maxx=4+4-2*(3+1)=0
# dfs(3, 2), l=4
# dfs(null, 3), return 3
# dfs(3, 2), l=4, r=3, return 4, maxx=4+3-2*(2+1)=1
# dfs(2, 1), l=4
# dfs(4, 2)
# dfs(null, 3), return 3
# dfs(4, 2), l=3
# dfs(null, 3), return 3
# dfs(4, 2), l=3, r=3, return 3, maxx=3+3-2*(2+1)=0
# dfs(2, 1), l=4, r=3, return 4, maxx=4+3-2*(1+1)=3
# dfs(1, 0), l=1, r=4
# return maxx=3
