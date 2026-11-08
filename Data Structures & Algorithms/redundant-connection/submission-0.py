class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

# [[1,2],[1,3],[3,4],[2,4]]
# parent=[0,1,2,3,4]
# [1,2], [0,2,2,3,4]
