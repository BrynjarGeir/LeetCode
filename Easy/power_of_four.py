class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 4 or n == 1: return True
        elif n < 0: return False
        
        while n >= 1:
            if n == 1: return True
            n /= 4
            if not n.is_integer(): return False
            else: n = int(n)