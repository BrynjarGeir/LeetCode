class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        def manhattan(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        validPoints = []
        for ind, point in enumerate(points):
            if point[0] == x or point[1] == y:
                validPoints.append((point, manhattan([x,y], point), ind))
        
        ans = sorted(validPoints, key = lambda x: (x[1], x[2]))
        if ans: return ans[0][2]
        return -1