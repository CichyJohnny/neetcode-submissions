from collections import deque

class Node:
        def __init__(self, val, after=set(), before=set(), visited=False):
            self.val = val
            self.after = set()
            self.before = set()
            self.visited = visited

class Solution:
    
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        for i in range(numCourses): # O(n)
            nodes[i] = Node(val=i)
        
        for n in prerequisites: # O(v)
            after = n[0]
            before = n[1]
            nodes[before].after.add(nodes[after])
            nodes[after].before.add(nodes[before])
        # {
        #  0: Node(0, [2], [])
        #  1: Node(1, [2,3], [])
        #  2: Node(2, [3], [0, 1])
        #  3: Node(3, [], [2,1])
        # }
        
        queue = deque()
        for n in nodes.values():
            if not n.before:
                queue.append(n)
        # queue = [0, 1]
        
        if not queue:
            return False

        while queue:
            node = queue.popleft()
            if node.visited or node.before:
                continue
            
            for n in node.after:
                n.before.remove(node)
                queue.append(n)
            node.visited = True
        # queue = [0, 1] 
        # Node(0, [2], []) -> Node(2, [3], [1])
        # queue = [1, 2]
        # Node(1, [2,3], []) -> Node(2, [3], []), Node(3, [], [2])
        # queue = [2, 2, 3]
        # Node(2, [3], []) -> Node(3, [], [2])
        # queue = [2, 3]
        # queue = [3]
        # Node(3, [], [])

        for n in nodes.values():
            if n.before:
                return False
        return True


# [2, 0] [2, 1] [3, 1] [3, 2]
#   2 - 3
# /  \ /
# 0   1

# [0, 1] [1, 2] [2, 1]
# 0 -> 1 <=> 2

# [0, 1]
# {0: Node(0, [], [1]), 1: Node(1, [0], [])}
# deque = [1]
# Node(1, [0], []) -> Node(0, [], [])
# deque = [0]
# Node(0, [], [])
