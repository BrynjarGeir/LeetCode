class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        countingSides = 0
        for ind, ver in enumerate(grid):
            for i, block in enumerate(ver):
                if block:
                    if i == 0 or grid[ind][i-1] == 0:
                        countingSides += 1
                    if i == len(ver)-1 or grid[ind][i+1] == 0:
                        countingSides += 1
                    if ind == 0 or grid[ind - 1][i] == 0:
                        countingSides += 1
                    if ind == len(grid)-1 or grid[ind+1][i] == 0:
                        countingSides += 1
        return countingSides
        