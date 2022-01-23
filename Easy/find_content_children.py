class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(); s.sort()
        n = len(g); m = len(s)
        cookie = 0; child = 0
        while cookie < m and child < n:
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child