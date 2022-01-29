class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxRectangle = max(rectangles, key = lambda x: min(x[0], x[1]))
        allMax = [r for r in rectangles if min(r[0],r[1]) == min(maxRectangle)]
        return len(allMax)