class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        x0 = coordinates[0][0]; y0 = coordinates[0][1]
        dx = coordinates[1][0] - x0
        dy = coordinates[1][1] - y0
        
        
        for i in range(2,len(coordinates)):
            if dx * (coordinates[i][1]-y0) != dy * (coordinates[i][0]-x0):
                return False
        return True