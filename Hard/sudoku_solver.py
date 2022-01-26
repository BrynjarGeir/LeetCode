import numpy as np
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
    def validMove(self, r, c, n):
        for i in range(9):
            if self.board[i][c] == n: return False
        for j in range(9):
            if self.board[r][j] == n: return False
        x, y = r - r%3, c - c%3

        for i in range(x, x+3):
            for j in range(y, y+3):
                if self.board[i][j] == n:
                    return False
        return True
    
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1
        
    def solve(self):
        row, col = self.findUnassigned()
        if row == col == -1:
            return True
        for n in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.validMove(row, col, n):
                self.board[row][col] = str(n)
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False
