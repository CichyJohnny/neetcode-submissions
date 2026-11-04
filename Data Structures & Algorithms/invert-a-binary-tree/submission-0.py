# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
        
    def invert(self, node: TreeNode):
        if not node:
            return
        node.left, node.right = node.right, node.left

        self.invert(node.left)
        self.invert(node.right)

# root = [1, 2,3, 4,5,6,7]
# invert(1), [1, 3,2, 6,7,4,5]
# invert(3), [1, 3,2, 7,6,4,5]
# invert(7), return
# invert(6), return
# invert(2), [1, 3,2, 7,6,5,4]
# invert(5), return
# invert(4), return
# return [1, 3,2, 7,6,5,4]