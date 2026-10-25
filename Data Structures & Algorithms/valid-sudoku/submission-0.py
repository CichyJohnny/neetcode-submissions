class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.areValidRows(board) and self.areValidColumns(board) and self.areValidSquares(board)
    
    def areValidRows(self, board):
        for row in board:
            unique = set()
            for r in row:
                if r != ".":
                    if r in unique:
                        print("Invalid row", row)
                        return False
                    unique.add(r)
        return True
    
    def areValidColumns(self, board):
        for col_id in range(len(board[0])):
            col = []
            for row in board:
                col.append(row[col_id])
            
            unique = set()
            for c in col:
                if c != ".":
                    if c in unique:
                        print("Invalid col", col)
                        return False
                    unique.add(c)
        return True
    
    def areValidSquares(self, board):
        for i in range(9):
            outer_row = i // 3
            outer_col = i % 3

            unique = set()
            for j in range(9):
                inner_row = outer_row * 3 + j // 3
                inner_col = outer_col * 3 + j % 3

                val = board[inner_row][inner_col]
                if val != ".":
                    if val in unique:
                        return False
                    unique.add(val)
        return True
