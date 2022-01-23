class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            chars = [int(c)*int(c) for c in str(n)]
            n = sum(chars)
            if n == 1: return True
            if n in seen: return False
            else: seen.add(n)
            
            