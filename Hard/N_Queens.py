from copy import deepcopy
class Solution:   
    
    solutions = []
    n = 0
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.n = 0
        if n == 1: return [['Q']]
        elif n == 2 or n == 3: return []
        self.n = n
        
        grid = [['.' for _ in range(n)] for _ in range(n)]
        solved = self.helper(n, 0, grid)
                
        ans = [[''.join(row) for row in sol] for sol in self.solutions]
        
        return ans
        
    def helper(self, n, row, grid):
        if n == row:
            self.solutions.append(deepcopy(grid))
            return True
        for col in range(n):
            if self.isValid(row, col, grid):
                grid[row][col] = 'Q'
                self.helper(n, row + 1, grid)
                grid[row][col] = '.'
        return False
    def isValid(self, row, col, grid):
        for i in range(row):
            if grid[i][col] == 'Q':
                return False
        (i, j) = (row, col)
        while i >= 0 and j >= 0:
            if grid[i][j] == 'Q':
                return False
            i -= 1; j -= 1
        (i, j) = (row, col)
        while i >= 0 and j  < self.n:
            if grid[i][j] == 'Q':
                return False
            i -= 1; j += 1
        return True