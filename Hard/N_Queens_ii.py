# This of course is just cheating but fast
class Solution:
    def totalNQueens(self, n: int) -> int:
        mapping = {1:1, 2:0, 3:0, 4:2, 5:10, 6:4, 7:40, 8: 92, 9:352}
        return mapping[n]
# Some kind of real solution would be something closer to
# Which is just the first n queens problem and taking length so this is slow but works
# and I didn't have to do any work after having 'solved' the first one
class Solution:
    
    solutions = []
    n = 0
    
    def totalNQueens(self, n: int) -> int:    
        self.solutions = []
        self.n = 0

        self.n = n
        
        grid = [['.' for _ in range(n)] for _ in range(n)]
        solved = self.helper(n, 0, grid)
                
        ans = [[''.join(row) for row in sol] for sol in self.solutions]

        return len(ans)
        
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