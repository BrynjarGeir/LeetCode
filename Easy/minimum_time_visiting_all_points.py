class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for ind, point in enumerate(points):
            if ind == len(points)-1: break
            x, y = point
            xT, yT = points[ind+1]
            while x!= xT or y!=yT:
                if x > xT: x -= 1
                elif x < xT: x += 1
                if y > yT: y -= 1
                elif y < yT: y += 1
                time += 1
        return time