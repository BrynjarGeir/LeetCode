class Solution:
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                else:
                    if self.isValid(i, j, board[i][j], board): continue
                    return False
        return True
    def isValid(self, r, c, n, board):
        for i in range(9):
            if board[i][c] == n and i != r: return False
        for j in range(9):
            if board[r][j] == n and j != c: return False
        x, y = r - r%3, c - c%3
        for i in range(x, x+3):
            for j in range(y, y+3):
                if board[i][j] == n and (i, j) != (r, c):
                    return False
        return True