class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        indexes = []; start, end, n = 0, 0, len(s)
        while start < n:
            while end < n and s[start] == s[end]:
                end += 1
            if end-start > 2: indexes.append([start,end-1])
            start = end
        return indexes