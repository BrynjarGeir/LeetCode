class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        elif n == 0: return 1
        elif n < 0: x = 1/x; n = -n
        
        y = 1
        while n:
            if n & 1:
                y *= x
            x *= x
            n >>= 1
        return y