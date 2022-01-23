class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3 or n == 1: return True
        elif n <= 0: return False
        
        while n > 1:
            n /= 3
            if n.is_integer(): n = int(n)
            else: return False
        return True