class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.fill(i, j, grid)
                    result += 1
        
        return result
    
    def fill(self, i, j, grid):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
            return
        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.fill(i - 1, j, grid)
        self.fill(i + 1, j, grid)
        self.fill(i, j - 1, grid)
        self.fill(i, j + 1, grid)



