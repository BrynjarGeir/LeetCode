from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        combs = combinations(points, 3)
        maxArea = -2**31
        for comb in combs:
            area = abs(0.5*(comb[0][0]*(comb[1][1]-comb[2][1]) + comb[1][0]*(comb[2][1] - comb[0][1]) + comb[2][0]*(comb[0][1] - comb[1][1])))
            if area > maxArea: maxArea = area
        return maxArea