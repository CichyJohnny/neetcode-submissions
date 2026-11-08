from collections import deque

class Node:
        def __init__(self, val, after=set(), before=set(), visited=False):
            self.val = val
            self.after = set()
            self.before = set()
            self.visited = visited

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = {}
        for i in range(numCourses):
            nodes[i] = Node(val=i)
        
        for n in prerequisites:
            after = n[0]
            before = n[1]
            nodes[before].after.add(nodes[after])
            nodes[after].before.add(nodes[before])
        
        queue = deque()
        for n in nodes.values():
            if not n.before:
                queue.append(n)
        
        if not queue:
            return []

        order = []

        while queue:
            node = queue.popleft()
            if node.visited or node.before:
                continue
            
            for n in node.after:
                n.before.remove(node)
                queue.append(n)
            node.visited = True
            order.append(node.val)

        for n in nodes.values():
            if n.before:
                return []
        return order
