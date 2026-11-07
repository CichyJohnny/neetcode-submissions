from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append([i, j])
        
        while queue:
            i, j = queue.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[ni])) or grid[ni][nj] == -1:
                    continue
                
                if grid[ni][nj] > grid[i][j] + 1:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append([ni, nj])
