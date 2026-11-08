class Solution:
    def solve(self, board: List[List[str]]) -> None:
        sys.setrecursionlimit(10000)

        rows = len(board)
        cols = len(board[0])

        self.board = board

        for i in range(rows):
            if board[i][0] == "O":
                self.isSurrounded(i, 0)
            if board[i][cols - 1] == "O":
                self.isSurrounded(i, cols - 1)
        
        for j in range(cols):
            if board[0][j] == "O":
                self.isSurrounded(0, j)
            if board[rows - 1][j] == "O":
                self.isSurrounded(rows - 1, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
     
    def isSurrounded(self, i, j):
        if not (0 <= i < len(self.board) and 0 <= j < len(self.board[0])):
            return
        
        if self.board[i][j] != "O":
            return
        
        self.board[i][j] = "E"

        self.isSurrounded(i - 1, j)
        self.isSurrounded(i + 1, j)
        self.isSurrounded(i, j - 1)
        self.isSurrounded(i, j + 1)
    
