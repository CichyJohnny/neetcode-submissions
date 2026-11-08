from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}
        for i in range(n):
            nodes[i] = []
        
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)
        
        # [[0,1],[0,2],[0,3],[1,4]]
        # {
        #  0: [1, 2, 3]
        #  1: [0, 4]
        #  2: [0]
        #  3: [0]
        #  4: [1]
        # }

        visited = set()
        queue = deque()
        queue.append((0, -1))
        while queue:
            pop = queue.popleft()
            val = pop[0]
            prev = pop[1]
            if val in visited: return False
            
            visited.add(val)

            neigh = nodes[val]
            for ne in neigh:
                if ne != prev:
                    queue.append((ne, val))
        
        # queue [(0, -1)], visited={}
        # queue [(0, 1), (1, 0), (2, 0), (3, 0)], visited={0}
        # queue [(1, 0), (2, 0), (3, 0)]
        
        return len(visited) == n

# [[0,1],[2,1],[3,2],[3,1],[4,1]]

#      4
#      |
# 0 -- 1 -- +
#      |    |
#      2 -- 3

# {0: [1], 1: [], 2: [1], 3: [1,2], 4: [1]}

# 