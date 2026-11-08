class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return

        pacific_reachable = set()
        atlantic_reachable = set()

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, reachable, prev_height):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if (r, c) in reachable:
                return
            if heights[r][c] < prev_height:
                return
            
            reachable.add((r, c))

            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])

        for i in range(rows):
            dfs(i, 0, pacific_reachable, heights[i][0])
        for i in range(cols):
            dfs(0, i, pacific_reachable, heights[0][i])
        
        for i in range(rows):
            dfs(i, cols-1, atlantic_reachable, heights[i][cols-1])
        for i in range(cols):
            dfs(rows-1, i, atlantic_reachable, heights[rows-1][i])
        
        return list(pacific_reachable & atlantic_reachable)