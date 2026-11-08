from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {}
        for i in range(n):
            nodes[i] = []
        
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)
        
        components = 0
        while nodes:
            queue = deque()
            for n in nodes.keys():
                queue.append(n)
                break
            
            while queue:
                print(queue)
                val = queue.popleft()
                if val not in nodes: continue
                neigh = nodes[val]

                for nei in neigh:
                    if nei in nodes:
                        queue.append(nei)
                nodes.pop(val)
            components += 1
        
        return components

# [[0,1],[1,2],[3,4]]
# {
# 0: [1]
# 1: [0, 2]
# 2: [1]
# 3: [4]
# 4: [3]
# }

# queue = [1], nodes={0,1,2,3,4}
# queue = [0,2], nodes={0,2,3,4}
# queue = [2], nodes={2,3,4}
# queue = [], nodes={3,4}
# components = 1
# queue = [3], nodes={3,4}
# queue = [4], nodes={4}
# queue = [], nodes={}
# components = 2
