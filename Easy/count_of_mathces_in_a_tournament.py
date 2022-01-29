class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1: return 0
        if n == 2: return 1
        if not n % 2:
            return self.numberOfMatches(n//2) + n//2
        else:
            return self.numberOfMatches((n-1)//2) + (n-1)//2 + 1