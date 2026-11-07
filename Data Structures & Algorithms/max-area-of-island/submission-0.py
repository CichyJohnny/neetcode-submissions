class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result = max(result, self.fill(i, j, grid))
        
        return result
    
    def fill(self, i, j, grid):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
            return 0
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        result = 1

        result += self.fill(i - 1, j, grid)
        result += self.fill(i + 1, j, grid)
        result += self.fill(i, j - 1, grid)
        result += self.fill(i, j + 1, grid)

        return result