"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        self.old_to_new = {}
        self.val_to_new = {}
        self.save(node)

        for old, new in self.old_to_new.items():
            for n in old.neighbors:
                new.neighbors.append(self.val_to_new[n.val])
        
        return self.old_to_new[node]



    def save(self, node):
        if node in self.old_to_new:
            return
        
        new = Node(val=node.val)
        self.old_to_new[node] = new
        self.val_to_new[node.val] = new

        for n in node.neighbors:
            self.save(n)