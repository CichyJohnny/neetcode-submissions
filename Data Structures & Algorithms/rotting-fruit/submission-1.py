from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        shortest = [[float("inf") for j in range(len(grid[i]))] for i in range(len(grid))]

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    shortest[i][j] = 0
        
        
        maxx = 0
        
        while queue:
            print(queue)
            i, j = queue.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                    continue
                
                if grid[ni][nj] == 0 or grid[ni][nj] == 2:
                    continue
                
                if shortest[ni][nj] > shortest[i][j] + 1:
                    shortest[ni][nj] = shortest[i][j] + 1
                    queue.append([ni, nj])
                    maxx = max(maxx, shortest[i][j] + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and shortest[i][j] == float("inf"):
                    return -1
        return maxx

# [[1,1,0],
#  [0,1,1],
#  [0,1,2]]
# queue = [[2,2]], shortest=[[inf,inf,inf],[inf,inf,inf],[inf,inf,0]]
# queue = [[1,2]], shortest=[[inf,inf,inf],[inf,inf,1],[inf,inf,0]]
# queue = [[1,2],[2,1]], shortest=[[inf,inf,inf],[inf,inf,1],[inf,1,0]]
# queue = [[2,1],[1,1]], shortest=[[inf,inf,inf],[inf,2,1],[inf,1,0]]
# queue = [[1,1]], shortest=[[inf,inf,inf],[inf,2,1],[inf,1,0]]
# queue = [[0,1]], shortest=[[inf,3,inf],[inf,2,1],[inf,1,0]]
# queue = [[0,0]], shortest=[[4,3,inf],[inf,2,1],[inf,1,0]]
# queue = [], shortest=[[4,3,inf],[inf,2,1],[inf,1,0]]

# [[2,1,1],
#  [0,1,1],
#  [1,0,1]]
# queue=[[0,0]], shortest=[[0,inf,inf],[inf,inf,inf],[inf,inf,inf]]
# queue=[[0,1]], shortest=[[0,1,inf],[inf,inf,inf],[inf,inf,inf]]
# queue=[[1,1]], shortest=[[0,1,inf],[inf,2,inf],[inf,inf,inf]]
# queue=[[1,1],[0,2]], shortest=[[0,1,2],[inf,2,inf],[inf,inf,inf]]
# queue=[[0,2],[1,2]], shortest=[[0,1,2],[inf,2,3],[inf,inf,inf]]
# queue=[[1,2]], shortest=[[0,1,2],[inf,2,3],[inf,inf,inf]]
# queue=[[2,2]], shortest=[[0,1,2],[inf,2,3],[inf,inf,4]]
# queue=[], shortest=[[0,1,2],[inf,2,3],[inf,inf,4]]
